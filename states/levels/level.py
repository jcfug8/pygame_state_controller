import pygame
from froggerlib import *
from states import state

#Base Level Class
class Level(state.State):

    def __init__(self, screen_height, screen_width, name):

        state.State.__init__(self, screen_height, screen_width, name)

        self.columns = 10
        self.rowHeight = self.screen_height // len(self.rows)
        self.columnWidth = self.screen_width // self.columns
        self.water = []
        self.road = []
        self.stage = []
        self.grass = []
        self.homes = []
        self.setRows()
        self.objectGap = 1
        self.frogX = self.columns // 2 * self.columnWidth + self.objectGap
        self.frogY = (len(self.rows) - 1) * self.rowHeight + self.objectGap
        self.frog = Frog(self.frogX, #x
                         self.frogY,#y
                         self.columnWidth - self.objectGap * 2, #w
                         self.rowHeight - self.objectGap * 2, #h
                         self.frogX, #dx
                         self.frogY,#dy
                         30, #s
                         self.columnWidth, #hg
                         self.rowHeight) #vg
        self.race_car = []
        self.dozer = []
        self.truck = []
        self.car = []
        self.log = []
        self.turtle = []
        self.setMovables()

    def setMovables(self):
        for i, row in enumerate(self.mov_pos):
            for j, move in enumerate(row):
                x = j * self.columnWidth
                y = i * self.rowHeight + self.objectGap
                w = self.columnWidth
                h = self.rowHeight - self.objectGap * 2
                dx = self.screen_width + 1
                if move == "l" or move == "d": #make the object twice as wide
                    w += w
                    dx += w
                if i % 2 == 0: # make every other row a different direction
                    dx = -1 - w
                if move == "t":
                    s = self.truckSpeed
                    self.turtle.append(Turtle(x, y, w, h, dx, y, s))
                elif move == "l":
                    s = self.logSpeed
                    self.log.append(Log(x, y, w, h, dx, y, s))
                elif move == "c":
                    s = self.carSpeed
                    self.car.append(Car(x, y, w, h, dx, y, s))
                elif move == "tr":
                    s = self.truckSpeed
                    self.truck.append(Truck(x, y, w, h, dx, y, s))
                elif move == "d":
                    s = self.dozerSpeed
                    self.dozer.append(Dozer(x, y, w, h, dx, y, s))
                elif move == "r":
                    mins = self.race_carSpeed[0]
                    maxs = self.race_carSpeed[1]
                    self.race_car.append(RaceCar(x, y, w, h, dx, y, mins, maxs))
                elif move == "h":
                    self.setHomes(j, i)

    def setHomes(self, j, i):
        x = j * self.columnWidth
        y = i * self.rowHeight
        w = self.columnWidth + self.columnWidth // 2
        h = self.rowHeight
        self.homes.append(Home(x, y, w, h))

    def logic(self, keys, newkeys, buttons, newbuttons, x, y):
        inHome = False
        self.playerMoveOff() #make sure player doesn't move the frog of screen
        self.moveFrog(newkeys) #move the frog
        #Check what the frog hits
        for water in self.water:
            if water.hits(self.frog):
                self.gameOver()
        for home in self.homes:
            if home.containsLocatable(self.frog):
                self.winGame()
                inHome = True
        for grass in self.grass:
            if grass.containsLocatable(self.frog) and not inHome:
                self.gameOver()
        for move in self.race_car:
            self.moveMovable(move)
            self.checkDodgeableHit(move)
        for move in self.dozer:
            self.moveMovable(move)
            self.checkDodgeableHit(move)
        for move in self.truck:
            self.moveMovable(move)
            self.checkDodgeableHit(move)
        for move in self.car:
            self.moveMovable(move)
            self.checkDodgeableHit(move)
        for move in self.log:
            self.moveMovable(move)
            move.supports(self.frog)
        for move in self.turtle:
            self.moveMovable(move)
            move.supports(self.frog)

    def playerMoveOff(self): #make sure the player can't move the frog of screen
        if self.frog.getDesiredX() > self.screen_width and not self.frog.riding():
            self.frog.setDesiredX(self.screen_width - self.frog.getWidth() - self.objectGap)
        if self.frog.getDesiredX() < 0 and not self.frog.riding():
            self.frog.setDesiredX(0 + self.objectGap)
        if self.frog.getDesiredY() > self.screen_height:
            self.frog.setDesiredY(self.screen_height - self.frog.getHeight() - self.objectGap)

    def winGame(self): #What to do when the game is won
        self.setNextState("Win Screen")

    def paint(self, surface):
        for row in self.grass:
            pygame.draw.rect(surface, (0,255,0), (row.getX(), row.getY(), row.getWidth(), row.getHeight()))
        for row in self.water:
            pygame.draw.rect(surface, (0,0,255), (row.getX(), row.getY(), row.getWidth(), row.getHeight()))
        for row in self.road:
            pygame.draw.rect(surface, (0,0,0), (row.getX(), row.getY(), row.getWidth(), row.getHeight()))
        for row in self.stage:
            pygame.draw.rect(surface, (255,0,255), (row.getX(), row.getY(), row.getWidth(), row.getHeight()))

        for move in self.race_car:
            pygame.draw.rect(surface, (150,0,0), (move.getX(), move.getY(), move.getWidth(), move.getHeight()))
        for move in self.dozer:
            pygame.draw.rect(surface, (150,30,30), (move.getX(), move.getY(), move.getWidth(), move.getHeight()))
        for move in self.truck:
            pygame.draw.rect(surface, (150,90,90), (move.getX(), move.getY(), move.getWidth(), move.getHeight()))
        for move in self.car:
            pygame.draw.rect(surface, (150,120,120), (move.getX(), move.getY(), move.getWidth(), move.getHeight()))
        for move in self.log:
            pygame.draw.rect(surface, (150,150,150), (move.getX(), move.getY(), move.getWidth(), move.getHeight()))
        for move in self.turtle:
            pygame.draw.rect(surface, (150,180,180), (move.getX(), move.getY(), move.getWidth(), move.getHeight()))
        for home in self.homes:
            pygame.draw.rect(surface, (200,200,200), (home.getX(), home.getY(), home.getWidth(), home.getHeight()))
        #Print the Frog
        pygame.draw.rect(surface, (255,255,255), (self.frog.getX(), self.frog.getY(), self.frog.getWidth(), self.frog.getHeight()))

    def moveFrog(self, newkeys):
        self.frog.move() # move the frog
        if pygame.K_UP in newkeys:
            self.frog.up()
        if pygame.K_DOWN in newkeys:
            self.frog.down()
        if pygame.K_LEFT in newkeys:
            self.frog.left()
        if pygame.K_RIGHT in newkeys:
            self.frog.right()
        if self.frog.outOfBounds(self.screen_width, self.screen_height): #if frog goes out of bounds
            self.gameOver()

    def moveMovable(self, move): #Move a movable object
        move.move()
        if move.outOfBounds(self.screen_width, self.screen_height):
            self.moveReset(move) #if it goes completely of the screen move it back

    def checkDodgeableHit(self, dodgeable): #Check if frog got hit by car
        if dodgeable.hits(self.frog):
            self.gameOver()

    def gameOver(self): #What to do when the player losses a game
        self.setNextState("End Screen")

    def moveReset(self, move): #Put the moving oject to the other side if it goes of the screen
        if move.getX() > self.screen_width: # right side
            move.setX(0 - move.getWidth())
        elif move.getX() < 0: # left side
            move.setX(self.screen_width)

    def setRows(self):
        rows = []
        x = 0
        y = 0
        w = self.screen_width
        h = self.rowHeight
        #create the rows based on self.rows that is first set
        for row in self.rows:
            if row == 's':
                self.stage.append(Stage(x, y, w, h))
            elif row == 'r':
                self.road.append(Road(x, y, w, h))
            elif row == 'w':
                self.water.append(Water(x, y, w, h))
            elif row == 'e':
                self.grass.append(Grass(x, y, w, h))
            y += h
