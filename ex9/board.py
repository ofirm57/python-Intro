#################################################################
# FILE : ex9.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex9 2020
#################################################################



class Board:
    """
    class responsible for all the things that happen on the board and all the
     information about the board is here
    """
    SIDE = 7
    EXIT_TARGET = (3, 7)

    def __init__(self):
        self.__side = Board.SIDE
        self.__cars = {}


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_str = ''
        bord_mat = self.get_mat_bord()
        for i, j in enumerate(bord_mat):
            if i == Board.EXIT_TARGET[0]:
                board_str += '$' + " ".join(j) + '→ \n'
            else:
                board_str += '$' + " ".join(j) + '$\n'
        return board_str


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        lst_of_cor = []
        side = self.__side
        for i in range(side):
            for j in range(side):
                lst_of_cor.append((i, j))
        lst_of_cor.append(Board.EXIT_TARGET)
        return lst_of_cor


    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # full_places - list with the tupls whos not free
        full_places = self.cars_board_coordinates()
        cell_list = self.cell_list()
        move_lst = []
        for car in self.__cars:
            car_dict_move = self.__cars[car].possible_moves()
            keys = car_dict_move.items()
            for movekey in keys:
                mast_be_empty = self.__cars[car].\
                    movement_requirements(movekey[0]) #
                if mast_be_empty[0] not in cell_list:
                    continue
                if mast_be_empty[0] in full_places:
                    continue
                form_tup = (car, movekey[0],  movekey[1])
                move_lst.append(form_tup)
        return move_lst


    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
         filled for victory.
        :return: (row,col) of goal location
        """
        return Board.EXIT_TARGET #In this board, returns (3,7)


    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.__cars:
            car_coordinates = self.__cars[car].car_coordinates()
            if coordinate in car_coordinates:
                return car
        return


    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        coor_new_car = car.car_coordinates()
        if not self.cars_board_coordinates():
            contained_coordinates = []
        else:
            contained_coordinates = self.cars_board_coordinates()
        cells = self.cell_list()
        for coordinate in coor_new_car:
            if coordinate in contained_coordinates:
                return False
            if coordinate not in cells:
                return False
        if car.get_name() in self.name_board_cars(): #repeat names check
            return False
        if not car.possible_moves():
            return False # orientation check
        self.__cars[car.get_name()] = car
        return True


    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # move_option form - [('O','d',"some description")..()]
        move_option = self.possible_moves()
        for i in move_option:
            if i[0] == name and i[1] == movekey:
                self.__cars[name].move(movekey)
                return True
        return False


    def cars_board_coordinates(self):
        """:return: list with tappel of all cars coordinates"""
        if not self.__cars:
            return []
        cars_board_coor = []
        for car_in_board in self.__cars:
            car_coordinates = self.__cars[car_in_board].car_coordinates()
            cars_board_coor.extend(car_coordinates)
        return cars_board_coor


    def get_mat_bord(self):
        """return list of list - the bord game (matrix) with the cars"""

        length = self.__side
        the_cars = self.__cars
        bord_lst = []
        for row in range(length):
            bord_lst.append(['_'] * length)# empty mat
        for car in the_cars:
            car_cor = self.__cars[car].car_coordinates() #form[(row,line)..()]
            for i in car_cor:
                bord_lst[i[0]][i[1]] = car # car = name =or ['O' or 'R'...]
        return bord_lst


    def name_board_cars(self):
        """return the car names that  in the bord """
        lst_of_cars_names = []
        for car in self.__cars:
            lst_of_cars_names.append(car)
        return lst_of_cars_names
