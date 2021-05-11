from ..utils.vector import Vector2


class Camera:       #donne une position et une échelle; rectangle sur un plan en gros 
    def __init__(self, screen_size):
        self.screen_size = screen_size  #vecteur de taille 2
        self.position = Vector2(0, 0)
        self.scale = 1      #echelle du monde par rapport à l'écran 

    def to_screen_coords(self, position):
        """ Converts the world-coordinate position to a screen-coordinate. """
<<<<<<< HEAD
        positionreduite = position * self.scale
        
=======
        screen_coord=position*self.scale+self.screen_size/2-self.position*self.scale
        return screen_coord
    
>>>>>>> faa663b2b3a0cc5a2feae4c67438d0f1830ee80e

    def from_screen_coords(self, position):
        """ Converts the screen-coordinate position to a world-coordinate. """
        raise NotImplementedError
