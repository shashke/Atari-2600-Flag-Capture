# level.py


class Level:
    """Base class for a level, which acts as a container for game objects"""

    def __init__(self):
        self.game_objects = [] # List that holds game objects

    def add_object(self, *objs):
        for obj in objs:
            self.game_objects.append(obj)

    def get_object(self, obj_id):
        found = []
        for obj in self.game_objects:
            if obj.id == obj_id:
                found.append(obj)
        
        if len(found) == 1:
            return found[0]
        return found

    def remove_object(self, obj_id):
        for obj in self.game_objects:
            if obj.id == obj_id:
                self.game_objects.remove(obj) 

    def tick(self, game):
        for obj in self.game_objects:
            obj.tick(game)