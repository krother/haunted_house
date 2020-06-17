"""Console script for haunted_house."""
import argparse
import sys
from haunted_house.house import create_rooms, inventory


def main():
    """Console script for haunted_house."""
    rooms = create_rooms()
    location = rooms["garden"]

    while True:
        print(f"you are in the {location}")
        print(location.description)  # calls the description() property function

        print("\nyou can go to:")
        location.print_connections()

        cmd = input("\nenter command: ")
        location = handle_command(cmd, rooms, location, inventory)

'''
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "haunted_house.cli.main")
    return 0
'''

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
