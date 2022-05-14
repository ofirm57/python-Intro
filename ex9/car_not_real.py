class Car:
    MOVES = {
        'u': "UP",
        'd': "DOWN",
        'l': "LEFT",
        'r': "RIGHT",
    }

    def __init__(self, name, length, location, orientation):
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation
        self.__coor = None
        if name == 'R':  # Round
            self.__coor = [tuple(location)]
        elif name == 'Y':  # Yashar
            self.__coor = [(i, location[1]) for i in range(location[0]-1,
                                                           location[0]+2)]
        elif name == 'G':  # Grow
            self.__coor = [tuple(location)]

    def car_coordinates(self):
        return self.__coor

    def possible_moves(self):
        return self.MOVES

    def movement_requirements(self, movekey):
        if self.__name == 'R': # Round
            return [(1,5)]
        elif self.__name == 'Y': # Yashar
            if movekey in ('r','l'):
                return [(loc[1], loc[0]) for loc in self.__coor
                        if (loc[1], loc[0]) not in self.__coor]
            if movekey in ('u',):
                return [(loc[0]-1, loc[1]-1) for loc in self.__coor
                        if (loc[0]-1, loc[1]-1) not in self.__coor]
            if movekey in ('d',):
                return [(loc[0]+1, loc[1]+1) for loc in self.__coor
                        if (loc[0]+1, loc[1]+1) not in self.__coor]
        elif self.__name == 'G': # Grow
            if movekey == 'r':
                return [(loc[0], loc[1] - 1) for loc in self.__coor
                        if (loc[0], loc[1] - 1) not in self.__coor]
            if movekey == 'l':
                return [(loc[0], loc[1] + 1) for loc in self.__coor
                        if (loc[0], loc[1] + 1) not in self.__coor]
            if movekey == 'u':
                return [(loc[0] - 1, loc[1]) for loc in self.__coor
                        if (loc[0] - 1, loc[1]) not in self.__coor]
            if movekey == 'd':
                return [(loc[0] + 1, loc[1]) for loc in self.__coor
                        if (loc[0] + 1, loc[1]) not in self.__coor]

    def move(self, movekey):
        if self.__name == 'Y': # Yashar
            if movekey in ('r','l'):
                self.__coor = [(loc[1], loc[0]) for loc in self.__coor]
            elif movekey in ('d',):
                self.__coor = [(loc[0]+1, loc[1]+1) for loc in self.__coor]
            elif movekey in ('u',):
                self.__coor = [(loc[0]-1, loc[1]-1) for loc in self.__coor]
        elif self.__name == 'G': # Grow
            if movekey == 'r':
                self.__coor = self.__coor + [(loc[0], loc[1] - 1) for loc in \
                        self.__coor if (loc[0], loc[1] - 1) not in self.__coor]
            if movekey == 'l':
                self.__coor = self.__coor + [(loc[0], loc[1] + 1) for loc in self.__coor
                                if (loc[0], loc[1] + 1) not in self.__coor]
            if movekey == 'u':
                self.__coor = self.__coor + [(loc[0] - 1, loc[1]) for loc in self.__coor
                                if (loc[0] - 1, loc[1]) not in self.__coor]
            if movekey == 'd':
                self.__coor = self.__coor + [(loc[0] + 1, loc[1]) for loc in self.__coor
                                if (loc[0] + 1, loc[1]) not in self.__coor]
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
