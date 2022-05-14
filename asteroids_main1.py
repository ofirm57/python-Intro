################################################
# FILE :asteroids_main.py
# WRITERS :Haim Kasel and Ofir Malkiely
# EXERCISE :10
# DESCRIPTION:Asteroids Game
################################################

import screen
import sys
import random
import math
import ship
import asteroid
import torpedo


COS = math.cos
SIN = math.sin
PI = math.pi


class GameRunner:
    DEFAULT_ASTEROIDS_NUM = 5
    ASTEROIDS_START_SIZE = 3
    START_POINTS = 0
    POINTS_DIC = {3: 20, 2: 50, 1: 100}
    LIFE_MSG = 'life', 'You Hit an asteroid, You Lost One life'
    END_GAME = 'End Game', 'You Chosen To End The Game'
    LOSE = 'Lose', 'You Lost The Game'
    WIN = 'Victory', 'Good, You Win!!!'
    MIN_ASTEROID_SIZE = 1


    def __init__(self, asteroids_amount):
        self.__screen = screen.Screen()
        self.__screen_max_x = screen.Screen.SCREEN_MAX_X
        self.__screen_max_y = screen.Screen.SCREEN_MAX_Y
        self.__screen_min_x = screen.Screen.SCREEN_MIN_X
        self.__screen_min_y = screen.Screen.SCREEN_MIN_Y
        self.__ship = ship.Ship(*self.random_location())
        self.__asteroids_lst = []
        self.load_asteroid(asteroids_amount, ())
        self.__torpedo = torpedo.Torpedo
        self.__torpedo_lst = []
        self.__points = START_POINTS


    def load_asteroid(self, num, data, size=ASTEROIDS_START_SIZE):
        """
        :param num: num of asteroids need to load to the game
        :param data: tuple of the coordinates of location and speed data
        :param size: num between 1 to 3
        add the asteroid to the list of asteroids and draw it on the screen
        """

        for i in range(num):
            if data:
                x_loc, y_loc, x_speed, y_speed = data[0], data[1], data[2], data[3]
            else:
                x_loc, y_loc = self.random_location()
                x_speed, y_speed = (
                    random.randint(1, 4), random.randint(1, 4))
            new_asteroids_obj = asteroid.Asteroid(x_loc, y_loc, x_speed,
                                                  y_speed, size)
            self.__asteroids_lst.append(new_asteroids_obj)
            self.__screen.register_asteroid(new_asteroids_obj, size)


    def random_location(self):
        """
        :return: tuple of 2 random location between the borders of the screen
        """
        return random.randint(self.__screen_min_x, self.__screen_max_x), \
               random.randint(self.__screen_min_y, self.__screen_max_y)


    def run(self):
        self._do_loop()
        self.__screen.start_screen()


    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)


    def ship_move_and_press(self):
        """
        check which buttons are pressed and change the location and the speed of the ship after pressing.
        """
        if self.__screen.is_right_pressed():
            self.__ship.set_direction(self.__ship.get_direction() - 7)
        if self.__screen.is_left_pressed():
            self.__ship.set_direction(self.__ship.get_direction() + 7)
        if self.__screen.is_up_pressed():
            new_x_speed = self._change_x_speed(self.__ship.get_x_speed(), self.__ship.get_direction())
            self.__ship.set_x_speed(new_x_speed)
            new_y_speed = self._change_y_speed(self.__ship.get_y_speed(),
                                               self.__ship.get_direction())
            self.__ship.set_y_speed(new_y_speed)
        move_x = self._move_object_x(self.__ship.get_x_speed(),
                                     self.__ship.get_x_location())
        self.__ship.set_x_location(move_x)
        move_y = self._move_object_y(self.__ship.get_y_speed(),
                                     self.__ship.get_y_location())
        self.__ship.set_y_location(move_y)


    def asteroid_move(self):
        """
        move the asteroids on the screen by calling the functions responsible for moving and
        check if asteroid hit by the ship or by the torpedo.
        """

        for asteroid in self.__asteroids_lst:
            self.__screen.draw_asteroid(asteroid, asteroid.get_x_location(), asteroid.get_y_location())
            new_x_loc = self._move_object_x(asteroid.get_x_speed(), asteroid.get_x_location())
            new_y_loc = self._move_object_y(asteroid.get_y_speed(), asteroid.get_y_location())
            asteroid.set_x_location(new_x_loc)
            asteroid.set_y_location(new_y_loc)

            if asteroid.has_intersection(self.__ship):
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids_lst.remove(asteroid)
                self.__screen.show_message(*LIFE_MSG)
                self.__screen.remove_life()
                self.__ship.set_life(self.__ship.get_life() - 1)

            for torpedo in self.__torpedo_lst:
                if asteroid.has_intersection(torpedo):
                    self.asteroid_intersection(torpedo, asteroid)




    def asteroid_intersection(self,torpedo, asteroid):
        """
        :param torpedo: torpedo object
        :param asteroid: asteroid object
        this function called after torpedo hit an asteroid, it remove the asteroid and make 2 asteroids if
        the size of the asteroid bigger than 1
        """
        self.__screen.unregister_torpedo(torpedo)
        self.__torpedo_lst.remove(torpedo)
        asteroid_speed = math.sqrt(asteroid.get_x_speed() ** 2 + asteroid.get_y_speed() ** 2)
        new_x_speed = (torpedo.get_x_speed() + asteroid.get_x_speed()) / asteroid_speed
        new_y_speed = (torpedo.get_y_speed() + asteroid.get_y_speed()) / asteroid_speed
        x_loc, y_loc = asteroid.get_x_location(), asteroid.get_y_location()
        new_astroid_data = (x_loc, y_loc, new_x_speed, new_y_speed)
        self.__points += POINTS_DIC[asteroid.get_size()]
        self.__screen.set_score(self.__points)

        if asteroid.get_size() > 1:
            x = asteroid.get_size() - 1
            self.load_asteroid(1, new_astroid_data, x)
            new_x_speed *= -1
            new_y_speed *= -1
            new_astroid_data = (x_loc, y_loc, new_x_speed, new_y_speed)
            self.load_asteroid(1, new_astroid_data, asteroid.get_size() - 1)
        if asteroid in self.__asteroids_lst:
            self.__screen.unregister_asteroid(asteroid)
            self.__asteroids_lst.remove(asteroid)


    def torpedo_move(self):
        """
        for every torpedo, set coordinates and call the functions responsible for moving.
        """
        for torpedo in self.__torpedo_lst:
            x_loc = torpedo.get_x_location()
            y_loc = torpedo.get_y_location()
            head = torpedo.get_direction()
            self.__screen.draw_torpedo(torpedo, x_loc, y_loc, head)

            new_x_loc = self._move_object_x(torpedo.get_x_speed(),
                                            torpedo.get_x_location())

            new_y_loc = self._move_object_y(torpedo.get_y_speed(),
                                            torpedo.get_y_location())
            torpedo.set_x_location(new_x_loc)
            torpedo.set_y_location(new_y_loc)
            torpedo.set_life(torpedo.get_life() - 1)
            if torpedo.get_life() == 0:
                self.__torpedo_lst.remove(torpedo)
                self.__screen.unregister_torpedo(torpedo)


    def load_torpedo(self):
        """
        check if space pressed and the number of the torpedoes smaller the 10,
        load torpedo object to the screen and add it to the torpedo list.
        """
        if self.__screen.is_space_pressed():
            if len(self.__torpedo_lst) < 10:
                x = self.__ship.get_x_location()
                y = self.__ship.get_y_location()
                x_speed = self.__ship.get_x_speed() + 2 * COS((self.__ship.get_direction() * (2 * PI)) / 360)
                y_speed = self.__ship.get_y_speed() + 2 * SIN((self.__ship.get_direction() * (2 * PI)) / 360)
                direction = self.__ship.get_direction()
                new_torpedo = torpedo.Torpedo(x, y, x_speed, y_speed, direction)
                self.__torpedo_lst.append(new_torpedo)
                self.__screen.register_torpedo(new_torpedo)


    def _game_loop(self):
        """
        call the functions of moving and loading objects every 5 milliseconds.
        """
        self.__screen.draw_ship(self.__ship.get_x_location(), self.__ship.get_y_location(), self.__ship.get_direction())
        self.ship_move_and_press() #
        self.asteroid_move()
        self.load_torpedo()
        self.torpedo_move()
        self.end_game()



    def end_game(self):
        """
        check if the player choose the end the game by pressing 'q'
        or if life is empty or if player hit all the asteroids. show the relevant massage to
        the player and end the game.
        """
        if self.__screen.should_end():
            self.__screen.show_message(*END_GAME)
            self.__screen.end_game()
            sys.exit()
        if self.__ship.get_life() == 0:
            self.__screen.show_message(*LOSE)
            self.__screen.end_game()
            sys.exit()

        if not self.__asteroids_lst:
            self.__screen.show_message(*WIN)
            self.__screen.end_game()
            sys.exit()


    def _move_object_x(self, object_speed_x, old_spot_x):
        """
        :param object_speed_x: the current speed in the x coordinate
        :param old_spot_x: the current location in x coordinate of the object
        :return: new x coordinate calculated by formula given in the exercise
        """
        new_spot_x = self.__screen.SCREEN_MIN_X + (old_spot_x + object_speed_x - self.__screen.SCREEN_MIN_X) % \
                     (self.__screen.SCREEN_MAX_X - self.__screen.SCREEN_MIN_X)

        return new_spot_x

    def _move_object_y(self, object_speed_y, old_spot_y):
        """
             :param object_speed_y: the current speed in the y coordinate
             :param old_spot_y: the current location in y coordinate of the object
             :return: new y coordinate calculated by formula given in the exercise
             """
        new_spot_y = self.__screen.SCREEN_MIN_Y + (old_spot_y + object_speed_y - self.__screen.SCREEN_MIN_Y) % \
                     (self.__screen.SCREEN_MAX_Y - self.__screen.SCREEN_MIN_Y)
        return new_spot_y

    def _change_x_speed(self, cur_x_speed, cur_der):
        """
             :param object_speed_x: the current speed in the x coordinate
             :param cur_der: the current direction of the object
             :return: new speed in x coordinate calculated by formula given in the exercise
             """
        new_x_speed = cur_x_speed + math.cos((cur_der * 2 * PI) / 360)
        return new_x_speed

    def _change_y_speed(self, cur_y_speed, cur_der):
        """
               :param object_speed_y: the current speed in the y coordinate
               :param cur_der: the current direction of the object
               :return: new speed in y coordinate calculated by formula given in the exercise
               """
        new_y_speed = cur_y_speed + math.sin((cur_der * 2 * PI) / 360)
        return new_y_speed


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)