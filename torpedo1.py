################################################
# FILE :torpedo.py
# WRITERS :Haim Kasel and Ofir Malkiely
# EXERCISE :10
# DESCRIPTION:Asteroids Game
################################################

TORPEDO_RADIUS = 4


class Torpedo():
    """ class that responsball about all the  """

    def __init__(self, x_location, y_location, x_speed, y_speed, direction=0, life= 200):
        self.__x_speed = x_speed  # int
        self.__y_speed = y_speed  # int
        self.__x_location = x_location  # int
        self.__y_location = y_location  # int
        self.__direction = direction  # float
        self.__life = life


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
        """
        :return: the radius of the torpedo
        """
        return TORPEDO_RADIUS

    def set_life(self, new_life):
        """
        set new life to the torpedo
        """
        self.__life = new_life

    def get_life(self):
        """
        :return: the life of the torpedo
        """
        return self.__life


