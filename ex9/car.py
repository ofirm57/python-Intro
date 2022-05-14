#################################################################
# FILE : ex9.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex9 2020
#################################################################

HORIZONTAL = 1 # l,r
VERTICAL = 0 # u,d
MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"


class Car:
    """
   This class has all the information about the car and the things that can
    be operated on the car
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location:tuple representing the car's head (row,col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation


    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        car_coordinat = [self.__location]
        row_num = car_coordinat[0][0]
        cole_num = car_coordinat[0][1]
        length = self.__length

        if self.__orientation == HORIZONTAL:
            for col_cord in range(length - 1):
                car_coordinat.append((row_num, cole_num + col_cord + 1))
            return car_coordinat

        elif self.__orientation == VERTICAL:
            for row_cord in range(length - 1):
                car_coordinat.append((row_num + row_cord + 1, cole_num))
            return car_coordinat


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.__orientation == HORIZONTAL:
            horizontal_movement = {'l': 'move the car left!',
                                   'r': 'move the car right!'}
            return horizontal_movement
        if self.__orientation == VERTICAL:
            vertical_movment = {'u': 'move the car up!',
                                'd': 'move the car down!'}
            return vertical_movment


    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """

        last_cord = self.car_coordinates()[-1]
        first_cord = self.car_coordinates()[0]
        if movekey == MOVE_DOWN:
            mast_be_empty = [(last_cord[0] + 1, last_cord[1])]
            return mast_be_empty

        elif movekey == MOVE_UP:
            mast_be_empty = [(first_cord[0] - 1, first_cord[1])]
            return mast_be_empty

        elif movekey == MOVE_RIGHT:
            mast_be_empty = [(last_cord[0], last_cord[1] + 1)]
            return mast_be_empty

        elif movekey == MOVE_LEFT:
            mast_be_empty = [(first_cord[0], first_cord[1] - 1)]
            return mast_be_empty


    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        loc = self.__location
        if self.__orientation == HORIZONTAL: # l,r
            if movekey == MOVE_RIGHT:
                self.__location = (loc[0], loc[1] + 1)
                return True
            elif movekey == MOVE_LEFT:
                self.__location = (loc[0], loc[1] - 1)
                return True
            else:
                return False

        elif self.__orientation == VERTICAL: # u,d
            if movekey == MOVE_UP:
                self.__location = (loc[0] - 1, loc[1])
                return True
            elif movekey == MOVE_DOWN:
                self.__location = (loc[0] + 1, loc[1])
                return True
            else:
                return False
        if movekey not in ['r', 'l', 'u', 'd']:
            return False


    def get_name(self):
        """:return: The name of this car.  """
        return self.__name
