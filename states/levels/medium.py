from states.levels import level

class Medium(level.Level):

    def __init__(self, screen_height, screen_width, name):
        self.rows = [
                        'e', 'w', 'w', 'w', 'w', 's', 'r', 'r', 'r', 'r', 's',
                    ]
        self.mov_pos = [
                        [' ', 'h', ' ', ' ', 'h', ' ', ' ', 'h', ' ', ' '],
                        ['t', ' ', ' ', 't', ' ', ' ', 't', ' ', ' ', ' '],
                        [' ', ' ', 'l', ' ', ' ', ' ', 'l', ' ', ' ', ' '],
                        [' ', ' ', 't', ' ', ' ', 't', ' ', ' ', 't', ' '],
                        ['l', ' ', ' ', 'l', ' ', ' ', ' ', 'l', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'c', ' ', ' ', 'c', ' ', ' ', 'c', ' '],
                        ['tr',' ', ' ', ' ', 'tr',' ', ' ', 'tr',' ', ' '],
                        ['d', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' '],
                        ['r', ' ', ' ', ' ', ' ', 'r', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ]
        self.race_carSpeed = [5, 20]
        self.dozerSpeed = 5
        self.truckSpeed = 10
        self.carSpeed = 10
        self.logSpeed = 12
        self.turtleSpeed = 10
        level.Level.__init__(self, screen_height, screen_width, name)
