################################################
# FILE : asteroid.py
# WRITERS :Haim Kasel and Ofir Malkiely
# EXERCISE :10
# DESCRIPTION:Asteroids Game
################################################

import math
ASTEROID_DEFAULT_SIZE = 3
ROOT = math.sqrt


class Asteroid:
    """
    Asteroid class, every asteroid have location and speed by coordinates in the screen and size
    """

    def __init__(self, x_location, y_location, x_speed, y_speed, size):
        self.__x_location = x_location  # int
        self.__y_location = y_location  # int
        self.__x_speed = x_speed  # int
        self.__y_speed = y_speed  # int
        self.__size = size  # int of 1 or 2 or 3


    def has_intersection(self, obj):
        """
        :param obj:ship or torpedo
        :return: True if the coordinates of the object equal to the coordinates of the asteroid and False else.
        """
        ob_x_loc, ob_y_loc = (obj.get_x_location(), obj.get_y_location())
        astro_x_loc, astro_y_loc = self.get_x_location(), self.get_y_location()

        asteroid_radius = (self.get_size() * 10) - 5
        distance = ROOT((ob_x_loc - astro_x_loc)**2+(ob_y_loc-astro_y_loc)**2)
        if distance <= asteroid_radius + obj.get_radus():
            return True
        return False
        

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


    def get_size(self):
        "Get the size of the asteroid"
        return self.__size

    def set_size(self, new_size):
        "change the size of the asteroid"
        self.__size = new_size

