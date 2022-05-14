#################################################################
# FILE : ex9.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex9 2020
#################################################################
import helper
import sys

MOVE_KEYS = ['u', 'd', 'l', 'r']
CAR_NAMES = ['G', 'B', 'R', 'Y', 'W', 'O']
WELCOME_MSG = 'for exit enter ! \n ' \
              'lets play -\n Please enter car name and movekey:'
EXIT = '!'
MOVE_PROBLEM = 'there was problem whit your move'
NEXT_TURN_MSG = 'next turn'
INCORRECT_INPUT_MSG = 'Incorrect input, try again!'
INCORRECT_VALUES_MSG = 'Incorrect car name or movekey, try again!'
WIN_MSG = 'CONGRATULATIONS YOU WON !!!!'


class Game:
    """
    This class has all the information about the game and responsible for
    the game play
    """

    def __init__(self, board, game_cars):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board
        self.__game_cars = game_cars
        for car in self.__game_cars:
            car_data = self.__game_cars[car]
            c_obj = Car(str(car), car_data[0], tuple(car_data[1]),car_data[2])
            if car in CAR_NAMES: #name check
                if 2 <= car_data[0] or car_data[0] <= 4: #length check
                    if self.__board.cell_content(tuple(car_data[1])) is None:
                        self.__board.add_car(c_obj)


    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """

        print(self.__board)
        user_choice = input(WELCOME_MSG) #type(user_choice)= str
        if user_choice == EXIT:
            return True
        if len(user_choice) != 3:
            print(INCORRECT_INPUT_MSG)
            return
        the_car, user_movekey = user_choice.split(',')  # enter to variable

        if the_car not in self.__game_cars or \
                user_movekey not in MOVE_KEYS:   #variable iligle
            print(INCORRECT_VALUES_MSG)
            return
        if self.__board.move_car(the_car, user_movekey):
            print(NEXT_TURN_MSG)
        else:
            print(MOVE_PROBLEM)


    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        target = self.__board.target_location()
        while self.__board.cell_content(target) is None: # if not win
            exit_game = self.__single_turn()
            if exit_game:
                break


if __name__ == "__main__":
    from board import *
    from car import *

    the_board = Board()
    game = Game(the_board, helper.load_json(sys.argv[1]))
    game.play()
