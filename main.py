import socket
import sys

from board import Board
from ship import Ship

guess_board = Board(10, 10)
created_board = Board(10, 10)
letter_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}


def coordinates_ships(board, health, name, number):
    dir_to_num = {'n': 0, 'e': 1, 's': 2, 'w': 3,
                  'N': 0, 'E': 1, 'S': 2, 'W': 3}

    position = input("Please type a coordinate for your " + name + " " + str(number) + ", for example A4: ")
    if health > 1:
        direction = input("Type a direction. (N: North, E: East, S: South, W: West): ")
    else:
        direction = 'S'
    any_ship = Ship((letter_to_num[position[0]] - 1, int(position[1]) - 1), dir_to_num[direction], health)
    if board.place_ship(any_ship) is True:
        board.place_ship(any_ship)
    else:
        print("Invalid coordinate(Overlap/Out of Map)")
        exit(1)
    board.print_board()


def coordinates_att():
    guess_board.print_board()
    attack_coordinates = input("Please enter a Coordinate you want to attack. (For Example: C4):")
    created_board.attack_ship(letter_to_num[attack_coordinates[0]], int(attack_coordinates[1]), guess_board)

print("Place your Ships. You have 4 different types of ships:"
      "\n"
      "\n- Titanic. 4 units long. 1 available."
      "\n- Cruiser. 3 units long. 2 available."
      "\n- Yacht. 2 units long. 3 available"
      "\n- Boat. 1 unit long. 4 available. \n")

created_board.print_board()

coordinates_ships(created_board, 4, "Titanic", 1)
coordinates_ships(created_board, 3, "Cruiser", 1)
coordinates_ships(created_board, 3, "Cruiser", 2)
coordinates_ships(created_board, 2, "Yacht", 1)
coordinates_ships(created_board, 2, "Yacht", 2)
coordinates_ships(created_board, 2, "Yacht", 3)
coordinates_ships(created_board, 1, "Boat", 1)
coordinates_ships(created_board, 1, "Boat", 2)
coordinates_ships(created_board, 1, "Boat", 3)
coordinates_ships(created_board, 1, "Boat", 4)

print("This is your final Board.\n")
print("Let's start guessing your Opponents Ships.")

while not created_board.game_over():
    coordinates_att()
