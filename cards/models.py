# Models for Cards package

class Card:
    """A simple Card class\n
    Initialize a Card object with the __init__ method.\n"""

    def __init__(self, name, type):
        # Instance properties
        self.name = name
        self.type = type

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type
