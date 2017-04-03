from states.menus import menu

class Instructions(menu.Menu):

    def __init__(self, screen_height, screen_width, name):

        self.menuItems = [
                        {"Text" : "Instructions", "Font" : 1, "Link": False, "Position" : {}},
                        {"Text" : "", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "Use the arrows to move around", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "-Don't get hit by a car", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "-Don't drown in the water", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "-Don't get lost in the grass", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "-You win when you make it into one", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "of the grey homes at the top of", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "the screen", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "Main Menu", "Font" : 0, "Link": "Main Menu", "Position" : {}}
                    ]
        menu.Menu.__init__(self, screen_height, screen_width, name)
