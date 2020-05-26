
# Haunted House
class Room:

    def __init__(self, name):
        """constructor"""
        self.name = name
        self.connections = []  # store other Room objects

    def add_connection(self, room):
        self.connections.append(room)
        room.connections.append(self)

    def print_connections(self):
        for i, loc in enumerate(self.connections, 1):
            print('\n'.join([f"{i} - {loc}" ]))

    def get_connected_room(self, number):
        return self.connections[number].name

    def __repr__(self):
        return self.name


rooms = [
    Room('garden'),
    Room('entrance'),
    Room('hallway'),
    Room('graveyard'),
    Room('staircase'),
    Room('cellar'),
    Room('tower'),
]
rooms = {r.name: r for r in rooms}  # dict comprehension

connections = [
    ('garden', 'entrance'),
    ('garden', 'graveyard'),
    ('entrance', 'hallway'),
    ('hallway', 'staircase'),
]
for r1, r2 in connections:
    rooms[r1].add_connection(rooms[r2])


location = rooms['garden']

while True:
   print(f'you are in the {location}')
   print('\nyou can go to:')
   location.print_connections()

   cmd = input('\nenter command: ')
   new_loc = rooms[location.get_connected_room(int(cmd)-1)]
   location = new_loc
