from states.menus import menu

class LevelMenu(menu.Menu):

    def __init__(self, screen_height, screen_width, name):

        self.menuItems = [
                        {"Text" : "What Level to Play", "Font" : 1, "Link": False, "Position" : {}},
                        {"Text" : "", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "Easy", "Font" : 0, "Link": "Easy", "Position" : {}},
                        {"Text" : "Medium", "Font" : 0, "Link": "Medium", "Position" : {}},
                        {"Text" : "Hard", "Font" : 0, "Link": "Hard", "Position" : {}},
                        {"Text" : "", "Font" : 0, "Link": False, "Position" : {}},
                        {"Text" : "Main Menu", "Font" : 0, "Link": "Main Menu", "Position" : {}}
                    ]
        menu.Menu.__init__(self, screen_height, screen_width, name)
