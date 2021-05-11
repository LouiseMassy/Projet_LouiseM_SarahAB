from ..utils.vector import Vector2


class Camera:       #donne une position et une échelle; rectangle sur un plan en gros 
    def __init__(self, screen_size):
        self.screen_size = screen_size  #vecteur de taille 2
        self.position = Vector2(0, 0)
        self.scale = 1      #echelle du monde par rapport à l'écran 

    def to_screen_coords(self, position):
        """ Converts the world-coordinate position to a screen-coordinate. """
        positionreduite = position * self.scale
        

    def from_screen_coords(self, position):
        """ Converts the screen-coordinate position to a world-coordinate. """
        raise NotImplementedError
