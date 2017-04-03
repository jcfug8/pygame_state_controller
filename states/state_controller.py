from states.menus import main_menu, end_screen, win_screen, level_menu, instructions
from states.levels import easy, medium, hard

class StateController:

    def __init__(self, screen_height, screen_width):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.states = self.loadStates()
        self.state = main_menu.MainMenu(screen_height, screen_width, "Main Menu")

    def logic(self, keys, newkeys, buttons, newbuttons, x, y):
        self.state.logic(keys, newkeys, buttons, newbuttons, x, y)
        if self.state.checkStateChange():
            newState = self.state.getNextState()
            self.state = self.states[newState](self.screen_height, self.screen_width, newState)


    def paint(self, surface):
        self.state.paint(surface)

    def loadStates(self):
        states = {}
        states["Main Menu"] = main_menu.MainMenu
        states["Instructions"] = instructions.Instructions
        states["Easy"] = easy.Easy
        states["Medium"] = medium.Medium
        states["Hard"] = hard.Hard
        states["End Screen"] = end_screen.EndScreen
        states["Win Screen"] = win_screen.WinScreen
        states["Level Menu"] = level_menu.LevelMenu
        return states
