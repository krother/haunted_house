
rooms = {
    'garden': ['entrance', 'graveyard'],
    'entrance': ['hallway'],
    'hallway': ['staircase', 'entrance'],
    'graveyard': ['garden'],
    'staircase': ['cellar', 'tower', 'hallway'],
    'cellar': ['staircase'],
    'tower': ['staircase'],
}

location = 'garden'

while True:
   print(f'you are in the {location}')
   print('\nyou can go to:')
   print('\n'.join([f"{i} - {loc}" for i, loc in enumerate(rooms[location], 1)]))

   cmd = input('\nenter command: ')
   new_loc = rooms[location][int(cmd)-1]
   location = new_loc
