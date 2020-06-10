# Haunted House

from haunted_house.item import inventory


class Room:
    def __init__(self, name, base_desc="", **kwargs):
        """constructor"""
        self.name = name
        self._base_desc = base_desc  # _ means this is meant to be private
        self.connections = []  # store other Room objects
        self.status = kwargs

    def add_connection(self, room):
        self.connections.append(room)
        room.connections.append(self)

    def print_connections(self):
        for i, loc in enumerate(self.connections, 1):
            print("\n".join([f"{i} - {loc}"]))

    def get_connected_room(self, number):
        return self.connections[number].name

    @property
    def description(self):
        result = self._base_desc
        if self.name == "graveyard" and self.status["skeletons_active"]:
            result += "\nthe skeletons move towards you"
        if self.name == "entrance":
            result += "\nthe door shuts behind you"
        result += "\n" + str(self.status)
        return result

    @staticmethod  # <-- swallows the self internally
    def turn_on_light():  # no self!!
        print(name)
        print("the lights are broken")

    def chase_skeletons_away(self):
        if self.name == "graveyard":
            print("the skeletons fall apart")
            self.status["skeletons_active"] = False

    def __repr__(self):
        return self.name


def create_rooms():
    rooms = [
        Room("garden", "it is full of dark violet flowers"),
        Room("entrance"),
        Room("hallway"),
        Room("graveyard", "there are three skeletons here", skeletons_active=True),
        Room("staircase"),
        Room("cellar"),
        Room("tower"),
    ]
    rooms = {r.name: r for r in rooms}  # dict comprehension

    connections = [
        ("garden", "entrance"),
        ("garden", "graveyard"),
        ("entrance", "hallway"),
        ("hallway", "staircase"),
        ("staircase", "tower"),
    ]
    for r1, r2 in connections:
        rooms[r1].add_connection(rooms[r2])
    return rooms


def handle_command(cmd, rooms, location, inventory):
    if cmd == "light":
        location.turn_on_light()
        # ^^^^^ jumps here ----^  (location becomes self)
    elif cmd == "boo":
        location.chase_skeletons_away()
    elif cmd.startswith("use"):
        itemname = cmd.split()[1]
        item = inventory[itemname]
        item.use(location)
    else:
        new_loc = rooms[location.get_connected_room(int(cmd) - 1)]
        location = new_loc
    return location


# main program
if __name__ == "__main__":
    rooms = create_rooms()
    location = rooms["garden"]

    while True:
        print(f"you are in the {location}")
        print(location.description)  # calls the description() property function

        print("\nyou can go to:")
        location.print_connections()

        cmd = input("\nenter command: ")
        location = handle_command(cmd, rooms, location, inventory)
