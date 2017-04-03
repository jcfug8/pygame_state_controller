from states.menus import menu

class EndScreen(menu.Menu):

    def __init__(self, screen_height, screen_width, name):

        self.menuItems = [
                        {"Text" : "Game Over", "Font" : 1, "Link": False, "Position" : {}},
                        {"Text" : "", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "Play Again", "Font" : 0, "Link": "Level Menu", "Position" : {}},
                        {"Text" : "Main Menu", "Font" : 0, "Link": "Main Menu", "Position" : {}}
                    ]
        menu.Menu.__init__(self, screen_height, screen_width, name)
