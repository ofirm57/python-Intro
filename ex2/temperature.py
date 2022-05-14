#################################################################
# FILE : temperature.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: check if the temperature is fine
#################################################################

def is_it_summer_yet(measure_temp, temp_d1, temp_d2, temp_d3):

    """function that accepts a certain threshold value (measure_temp)
     and tell you if two from three next days the temperature
     was higher then measure_temp """

    if measure_temp < (temp_d1 and (temp_d2 or temp_d3)):
        return True

    elif measure_temp < (temp_d2 and (temp_d1 or temp_d3)):
        return True

    elif measure_temp < (temp_d3 and (temp_d1 or temp_d2)):
        return True

    else:
        return False
