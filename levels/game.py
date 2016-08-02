# game.py
from .level import Level

class GameLevel(Level):
    """The Flag Capture game."""

    def __init__(self):
        Level.__init__(self)

    def tick(self, game):
        self.logic(game)
        self.draw(game.screen)
        Level.tick(self, game)

    def logic(self, game):
        pass
    
    def draw(self, screen):
        pass