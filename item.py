"""
TODO: Items have a specific effect when they are activated in a specific room.
"""
import sys


# item 1: key
# effect: if the item is activated in the entrance, it opens the door
def activate_key(room):
    """room is a Room object"""
    if room.name == "entrance":
        print("the door has been opened")
        room.status["door"] = "open"


# item 2: silver orb
# effect: if the item is activated in the tower, it wins the game
def activate_orb(room):
    """Game-winning object"""
    if room.name == "tower":
        print("you win the game")
        sys.exit(0)


# we have several options to implement that behaviour


class Item:
    """option 3: one generic item class + callback functions"""

    def __init__(self, name, callback):
        self.name = name
        self.callback = callback  # free-floating function that I define elsewhere

    def __repr__(self):
        return self.name

    def use(self, room):
        """calls the callback function"""
        self.callback(room)


key = Item("key", activate_key)
orb = Item("silver orb", activate_orb)

inventory = {"key": key, "orb": orb}

"""
# option 1: subclasses

class Item:
    ...


class Key(Item):

    def use(self, room):
        if room.name == 'entrance':
            print('the door has been opened')
            room.status['door'] = 'open'

class SilverOrb(Item):
    ...

# most of the time: subclassing is overkill


# option 2: model all possible behaviours in a generic way
class Item:

   def __init__(self):
       self.kills_skeletons = False
       self.opens_the_door = False
       self.wins_the_game = True
# maybe a bit inflexible
"""
