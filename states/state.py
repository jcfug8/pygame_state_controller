#base state class

class State:

    def __init__(self, screen_height, screen_width, name):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.stateName = name
        self.nextState = ""
        self.stateChange = False

    def checkStateChange(self):
        return self.stateChange

    def getNextState(self):
        return self.nextState

    def setNextState(self, nextState):
        self.nextState = nextState
        self.stateChange = True
