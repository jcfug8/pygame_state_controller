from states.levels import level

class Easy(level.Level):

    def __init__(self, screen_height, screen_width, name):
        self.rows = [ #sets up the rows
                        'e', 'w', 'w', 'w', 'w', 's', 'r', 'r', 'r', 'r', 's',
                    ]
        self.mov_pos = [ #sets up the positions for objects
                        [' ', 'h', ' ', ' ', 'h', ' ', ' ', 'h', ' ', ' '],
                        ['t', ' ', 't', ' ', 't', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'l', ' ', ' ', ' ', 'l', ' ', ' ', ' '],
                        [' ', ' ', 't', ' ', ' ', 't', ' ', 't', ' ', ' '],
                        ['l', ' ', ' ', 'l', ' ', ' ', 'l', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', 'r', ' ', ' ', ' ', ' '],
                        ['tr',' ', ' ', ' ', 'tr',' ', ' ', 'tr',' ', ' '],
                        ['d', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'c', ' ', ' ', ' ', ' ', 'c', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ]
        #set up speeds
        self.race_carSpeed = [2, 10]
        self.dozerSpeed = 3
        self.truckSpeed = 7
        self.carSpeed = 7
        self.logSpeed = 8
        self.turtleSpeed = 4
        level.Level.__init__(self, screen_height, screen_width, name)
