from states.levels import level

class Hard(level.Level):

    def __init__(self, screen_height, screen_width, name):
        self.rows = [
                        'e', 'w', 'w', 'w', 'w', 's', 'r', 'r', 'r', 'r', 's',
                    ]
        self.mov_pos = [
                        [' ', 'h', ' ', ' ', 'h', ' ', ' ', 'h', ' ', ' '],
                        ['t', ' ', 't', ' ', ' ', 't', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'l', ' ', ' ', ' ', 'l', ' ', ' ', ' '],
                        ['l', ' ', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' '],
                        [' ', ' ', ' ', 't', ' ', 't', ' ', 't', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        ['d', ' ', ' ', ' ', ' ', 'd', ' ', ' ', 'd', ' '],
                        [' ', ' ', 'c', ' ', ' ', 'c', ' ', ' ', 'c', ' '],
                        ['r', ' ', ' ', ' ', ' ', 'r', ' ', ' ', 'r', ' '],
                        ['tr',' ', ' ', ' ', 'tr',' ', ' ', 'tr',' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ]
        self.race_carSpeed = [10, 20]
        self.dozerSpeed = 7
        self.truckSpeed = 15
        self.carSpeed = 12
        self.logSpeed = 15
        self.turtleSpeed = 13
        level.Level.__init__(self, screen_height, screen_width, name)
