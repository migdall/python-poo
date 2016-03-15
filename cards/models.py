# Models for Cards package

class Card:
    """A simple Card class\n
    Initialize a Card object with the __init__ method.\n"""

    def __init__(self, name, type):
        # Instance properties
        self.name = name
        self.type = type

    def __repr__(self):
        return "%s Card of type %s" % (self.name, self.type)

    def __str__(self):
        return "%s Card" % self.name

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

class PooCard (Card):
    """ Poo Card class that inherits from the class Card\n
    Initialize a PooCard object with the __init__ method.\n"""

    def __init__(self, name, damage):
        # Initialize the Card properties
        Card.__init__(self, name, "POO")
        self.damage = damage

    def get_damage(self):
        return self.damage
