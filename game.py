"""

Pong game

"""
import sys, pygame
import utils.colors as color
from levels.main_menu import MainMenuLevel
from levels.flag_menu import FlagMenuLevel
from levels.game import GameLevel
from config import SIZE

# Game type constants
FFA = "FFA"
D2P = "D2P"
S2P = "S2P"
T1P = "T1P"
FLAG_MENU = "FLAG_MENU"
MAIN_MENU = "MAIN_MENU"

GAME = "GAME"

# Flag type constants
FLAG_STATIONARY = "STATIONARY"
FLAG_M_WALL = "M_WALL"
FLAG_M_WRAPAROUND = "M_WRAPAROUND"

class Game:

    def __init__(self):
        # Initialize game
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Atari 2600 Flag Capture")
        
        self.game_type = None
        self.flag_type = None

        # Intro level
        self.level = MainMenuLevel()

        # Game loop
        while 1:
            self.tick()

    def tick(self):
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        self.level.tick(self)

        pygame.display.flip() # Buffer

    def change_level(self, level):
        if level == MAIN_MENU:
            self.level = MainMenuLevel()
        elif level == FLAG_MENU:
            self.level = FlagMenuLevel()
        elif level == GAME:
            self.level = 


if __name__ == "__main__":
    Game()