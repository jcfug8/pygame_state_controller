from states.menus import menu

class MainMenu(menu.Menu):

    def __init__(self, screen_height, screen_width, name):

        self.menuItems = [
                        {"Text" : "Frogger", "Font" : 1, "Link": False, "Position" : {}},
                        {"Text" : "", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "Play", "Font" : 0, "Link": "Level Menu", "Position" : {}},
                        {"Text" : "How to Play", "Font" : 0, "Link": "Instructions", "Position" : {}}
                    ]
        menu.Menu.__init__(self, screen_height, screen_width, name)
