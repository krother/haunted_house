
from house import create_rooms, handle_command, inventory
import pytest

# TODO
# 1) fixture
# 2) parametrized test
# 3) test coverage
# 4) TravisCI

# fixture is a function preparing test data
@pytest.fixture
def rooms():
    return create_rooms()    # state before


def test_move(rooms):
    """if I enter the command '1', the player moves to a different room."""
    room_after = handle_command('1', rooms, rooms["garden"], inventory)   # operation under test
    assert room_after.name != "garden"    # assert on the state after


def test_wrong_move(rooms):
    """non-existing command should result in a crash"""
    pytest.raises(ValueError, handle_command, 'x', rooms, rooms["garden"], inventory)
    #try:
    #    handle_command('x', rooms, rooms["garden"], inventory)
    #    assert False
    #except ValueError:
    #    assert True


EXAMPLES = [
    ("122", "staircase"),
    ("2", "graveyard"),
    ("12", "hallway"),
    ("21", "garden")
]

@pytest.mark.parametrize(('path', 'expected_destination'), EXAMPLES)
def test_multiple_moves(rooms, path, expected_destination):
    location = rooms["garden"]
    for cmd in path:
        location = handle_command(cmd, rooms, location, inventory)   # operation under test
    assert location.name == expected_destination
