"""The base file Module"""

class Base:
    """The base class"""
    __nb_objects = 0


    def __init__(self, id=None):
        """The Method used for Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects