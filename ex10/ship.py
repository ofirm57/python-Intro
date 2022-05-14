################################################
# FILE : ship.py
# WRITER :
# EXERCISE: intro2cs2 ex10 2020
# DESCRIPTION:
################################################

import math
PI = math.pi


class Ship:
    """ All variables and information about Ship Are in this class"""

    SHIP_RADIUS = 1

    def __init__(self, x_location, y_location, direction=0, x_speed=0,
                 y_speed=0, lives=3):
        self.__x_speed = x_speed  # int
        self.__y_speed = y_speed  # int
        self.__x_location = x_location  # int
        self.__y_location = y_location  # int
        self.__direction = direction  # float
        self.__lives = lives

    def get_x_speed(self):
        """
        :return: the speed on x
        """
        return self.__x_speed

    def get_y_speed(self):
        """
        :return: the speed on y
        """
        return self.__y_speed

    def set_x_speed(self, new_x_speed):
        """
        changes the speed on x
        """
        self.__x_speed = new_x_speed

    def set_y_speed(self, new_y_speed):
        """
        changes the speed on y
        """
        self.__y_speed = new_y_speed

    def get_x_location(self):
        """
        :return: the location on x
        """
        return self.__x_location


    def get_y_location(self):
        """
        :return: the location on y
        """
        return self.__y_location


    def set_x_location(self, new_x_location):
        """
        changes the speed on x
        """
        self.__x_location = new_x_location


    def set_y_location(self, new_y_location):
        """
        changes the speed on x
        """
        self.__y_location = new_y_location


    def get_direction(self):
        """
        :return: the direction of the ship
        """
        return self.__direction


    def set_direction(self, new_direction):
        """
        changes the direction
        """
        self.__direction = new_direction


    def get_radus(self):
        """get the radius"""
        return Ship.SHIP_RADIUS


    def get_life(self):
        """ get the value of life"""
        return self.__lives


    def set_life(self, new_life):
        """change the life"""
        self.__lives = new_life
