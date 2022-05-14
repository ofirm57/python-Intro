################################################
# File: hanoi.py
# Writer: Dor Roter
# Login: dor.roter
# Exercise: ------
# More:
#       Consulted: -----
#       Internet:
#       Notes:
################################################
import sys


class MockHanoi:
    def __init__(self):
        self.counter = 0
        self.moves = list()

    def move(self, src, dst):
        self.counter += 1
        self.moves.append((src, dst))

    def is_minimum(self, i):
        if i >= 1:
            return self.counter == ((2 ** i) - 1)
        else:
            return self.counter == 0

    # returns false if any moves where wrong
    def _run(self, disks):
        towers = dict()
        towers['A'] = [i for i in range(disks, 0, -1)]
        towers['B'] = list()
        towers['C'] = list()

        FROM = 0
        TO = 1
        for move in self.moves:
            disk = towers[move[FROM]].pop()
            if len(towers[move[TO]]) > 0 and \
                    disk > towers[move[TO]][-1]:
                # larger disk
                return False
            towers[move[TO]].append(disk)

        if len(towers['A']) == 0 and (len(towers['B']) == disks or
                                      len(towers['C']) == disks):
            return True
        return False

    def validate_moves(self, disks):
        if not self.moves or disks <= 0:
            return self.counter == 0
        try:
            return self._run(disks)
        except:
            print(sys.exc_info()[0])
            return False
