import pygame
from states import state

#Base Menu class
class Menu(state.State):

    def __init__(self, screen_height, screen_width, name):
        state.State.__init__(self, screen_height, screen_width, name)
        self.fonts = [pygame.font.SysFont('Comic Sans MS', 30),
                      pygame.font.SysFont('Comic Sans MS', 45)] #create a library of different fonts
        self.setPositions()
        self.selection = None
        self.changeSelection()
        self.arrow_width = 15
        self.arrow_height = 30
        self.menuItemPadding = 5


    def logic(self, keys, newkeys, buttons, newbuttons, x, y):
        self.changeSelection(newkeys)
        if pygame.K_RETURN in newkeys:#if the user hits enter, change the state
            nextState = self.menuItems[self.selection]["Link"]
            self.setNextState(nextState)

    def paint(self, surface):
        for i, item in enumerate(self.menuItems):
            #set up everything to print the text
            font = self.fonts[item["Font"]]
            text = item["Text"]
            x, y = item['Position']["x"], item['Position']["y"]
            textsurface = font.render(item["Text"], False, (255, 0, 0))
            #print the text
            surface.blit(textsurface, (x, y))
            if i == self.selection: #if the items being printed is also the current selected item
                #set the arrow positions
                x1 = item['Position']['x'] - self.arrow_width - self.menuItemPadding
                x2 = item['Position']['x'] + item['Position']['width'] + self.arrow_width + self.menuItemPadding
                y1 = item['Position']['y'] + (item['Position']['height'] - self.arrow_height)//2
                y2 = y1 + self.arrow_height//2
                y3 = y1 + self.arrow_height
                #draw the arrows
                pygame.draw.polygon(surface, (255,0,0), [(x1, y1), (x1 + self.arrow_width, y2), (x1, y3)])
                pygame.draw.polygon(surface, (255,0,0), [(x2, y1), (x2 - self.arrow_width, y2), (x2, y3)])

    def setPositions(self):
        totalHeight = 0
        yPositions = []
        for item in self.menuItems:
            font = self.fonts[item["Font"]]
            text = item["Text"]
            #get rendered font size
            width, height = font.size(text)
            #set items x position and width and height
            item["Position"]['x'] = self.screen_width//2 - width//2
            item["Position"]['width'], item["Position"]['height'] = width, height
            #put items y position into an array which will later be adjusted for vertical centering
            yPositions.append(totalHeight)
            #add current items height to menu's total height
            totalHeight += height
        #set what to offset the y posistion to make the menu vertically centered
        yOffSet = self.screen_height//2 - totalHeight//2
        for item, y in zip(self.menuItems, yPositions):
            item["Position"]["y"] = y + yOffSet

    def changeSelection(self, newkeys = []):
        #set selection to first item with a link
        if self.selection == None:
            for i, item in enumerate(self.menuItems):
                if item["Link"] != False:
                    self.selection = i
                    break
        #if user hits up
        if pygame.K_UP in newkeys:
            temp_select = self.selection
            for i in range(len(self.menuItems)):
                if temp_select - 1 == -1: #at the top of the list already
                    temp_select = len(self.menuItems) - 1
                else: #in the middle
                    temp_select -= 1
                if self.menuItems[temp_select]["Link"] != False:#checks to make sure only items with links can be selected
                    self.selection = temp_select
                    break
        #if user hits down
        if pygame.K_DOWN in newkeys:
            temp_select = self.selection
            for i in range(len(self.menuItems)):
                if temp_select + 1 > len(self.menuItems) - 1: #at the bottom of the list already
                    temp_select = 0
                else: #in the middle
                    temp_select += 1
                if self.menuItems[temp_select]["Link"] != False:#checks to make sure only items with links can be selected
                    self.selection = temp_select
                    break
