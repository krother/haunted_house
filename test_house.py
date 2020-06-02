
from house import create_rooms, handle_command, inventory
import pytest


def test_lists():
    actual = [1,2, 3, 4, 5]
    expected = [1,2,7,4,5]
    assert actual == expected

def test_move():
    """
    if I enter the command '1', the player moves to a different room.
    """
    rooms = create_rooms()    # state before
    room_after = handle_command('1', rooms, rooms["garden"], inventory)   # operation under test
    assert room_after.name != "garden"    # assert on the state after


def test_wrong_move():
    """non-existing command should result in a crash"""
    rooms = create_rooms()
    pytest.raises(ValueError, handle_command, 'x', rooms, rooms["garden"], inventory)
    #try:
    #    handle_command('x', rooms, rooms["garden"], inventory)
    #    assert False
    #except ValueError:
    #    assert True


def test_multiple_moves():
    rooms = create_rooms()
    location = rooms["garden"]
    for cmd in "122":
        location = handle_command(cmd, rooms, location, inventory)   # operation under test
    assert location.name == 'staircase'
