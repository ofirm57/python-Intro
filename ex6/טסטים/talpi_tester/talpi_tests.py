from .autotest import TestSet

from . import testrunners

import wave_helper
import sys
from importlib import import_module
from io import StringIO

def setup_runner(modulename, fname, args=[], kwargs={}, options={},tname=''):
    try:
        _stdout = sys.stdout
        tmpout = StringIO()
        module = import_module(modulename)
        func = getattr(module, fname)
        sys.stdout = tmpout

        setupopt = options.pop('setup')

        wave_helper.set_setup(setupopt)

        retval = testrunners.input_runner(modulename, fname, args, kwargs, options)
        sys.stdout = _stdout

        wave = [wave_helper.saved_fs, wave_helper.saved_data]

        return None, wave

    finally:
        sys.stdout = _stdout

defaults = {'modulename':'wave_editor'}


cases = {}
for k in wave_helper.stps.keys():
    stp = wave_helper.stps[k]
    cases[k] = {'fname': 'full_main',
        'runner': setup_runner,
        'args': [],
        'ans': [[stp["res_fs"], stp["res_data"]]],
        'options': {
            'setup': k,
            'input': stp["input"],
        },

    }



tsets = {'wave_editor':TestSet({},cases)}
