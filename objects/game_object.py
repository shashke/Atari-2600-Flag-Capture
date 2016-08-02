# game_object.py


class GameObject:
    """Base class for a game object."""

    def __init__(self, obj_id, x, y):
        self.id = obj_id
        self.x = x
        self.y = y

    def tick(self, game):
        self.logic()
        self.draw(game.screen)

    def logic(self):
        pass

    def draw(self, screen):
        pass

