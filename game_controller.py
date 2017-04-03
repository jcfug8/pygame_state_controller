import pygame
import math
import game_mouse
from states.state_controller import StateController

# Starter code for PyGame applications

class GameController(game_mouse.Game):

    def __init__(self, width, height, fps):
        pygame.font.init()

        game_mouse.Game.__init__(self, "Pygame Starter", width, height, fps)

        self.state_controller = StateController(height, width)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        self.state_controller.logic(keys, newkeys, buttons, newbuttons, x, y)
        return

    def paint(self, surface):
        surface.fill((255,255,255))
        self.state_controller.paint(surface)
        return

def main():
    screen_width = 660
    screen_height = 693
    frames_per_second = 10
    game = GameController(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return

if __name__ == "__main__":
    main()
