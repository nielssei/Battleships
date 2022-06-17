from battleship_setup import *
guess_board = [[], [], [], [], [], [], [], []]
for i in range(8):
    guess_board[i].append('0')
    for j in range(8):
        guess_board[j].append('0')

created_board = [[], [], [], [], [], [], [], []]
for i in range(8):
    created_board[i].append('0')
    for j in range(8):
        created_board[j].append('0')

letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
tries = 0

print("Place your Ships. You have 4 different types of ships:"
      "\n"
      "\n- Titanic. 4 units long. 1 available."
      "\n- Cruiser. 3 units long. 2 available."
      "\n- Yacht. 2 units long. 3 available"
      "\n- Boat. 1 unit long. 3 available. \n")

titanic_1 = Ship("Titanic", "1")
cruiser_1 = Ship("Cruiser", "1")
cruiser_2 = Ship("Cruiser", "2")
yacht_1 = Ship("Yacht", "1")
yacht_2 = Ship("Yacht", "2")
yacht_3 = Ship("Yacht", "3")
boat_1 = Ship("Boat", "1")
boat_2 = Ship("Boat", "2")
boat_3 = Ship("Boat", "3")

titanic_1.place_ship(created_board)
cruiser_1.place_ship(created_board)
cruiser_2.place_ship(created_board)
yacht_1.place_ship(created_board)
yacht_2.place_ship(created_board)
yacht_3.place_ship(created_board)
boat_1.place_ship(created_board)
boat_2.place_ship(created_board)
boat_3.place_ship(created_board)

print("\n   0 1 2 3 4 5 6 7 ")
row_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(8):
    line = row_index[i] + " |"
    for j in range(8):
        line += created_board[i][j]
        line += "|"
    print(line)

print("This is your final board.")
print("\nLet's start guessing your Opponents ships. You have 10 tries.")
while tries < 10:
    print("   0 1 2 3 4 5 6 7 ")
    row_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in range(8):
        line = row_index[i] + " |"
        for j in range(8):
            line += guess_board[i][j]
            line += "|"
        print(line)

    locationInput = input("Enter a Location (e.g. A3): ")

    rowInput = int(letter_to_number[locationInput[0]])
    colInput = int(locationInput[1])

    if colInput < 8 and rowInput < 8:
        if created_board[rowInput][colInput] == 'X':
            guess_board[rowInput][colInput] = 'X'
            tries += 1
            print('\nYou hit a ship! ' + str(10 - tries) + ' tries left\n')
        else:
            guess_board[rowInput][colInput] = '-'
            tries += 1
            print('\nNo ships hit... ' + str(10 - tries) + ' tries left\n')
    else:
        print('\nNUMBER(S) OUT OF RANGE. PLEASE TYPE A NUMBER BETWEEN 0 and 7\n')
