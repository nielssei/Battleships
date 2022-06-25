import socket
import sys
import time
from os import system

from board import Board
from ship import Ship


class Context:
    def __init__(self, ip, port, name):
        self.ip = ip
        self.port = port
        self.name = name


class Server:
    def __init__(self, context: Context):
        self.context = context

    def receive(self):
        # create new socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((str(self.context.ip), int(self.context.port)))
        self.socket.listen()

        (conn, addr) = self.socket.accept()

        # receive message
        data = conn.recv(500)
        message = data.decode()

        # send reply
        conn.sendall(f"ack {message}".encode())

        conn.close()
        self.socket.close()

        return message


class Client:
    def __init__(self, context: Context):
        self.context = context

    def send(self, message):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self.remote)

        # handle initial connection -> send this server's ip and address for auto-connect
        if message.startswith("init"):
            message = message + " " + self.context.name + " " + self.socket.getsockname()[0] + " " + self.context.port

        self.socket.sendall(message.encode())

        # receive send reply, not used at the moment
        data = self.socket.recv(500)
        #message = data.decode()
        #print(f"Received: {message}")

        self.socket.close()

    # send initial connection request
    def init(self, remoteIp, remotePort):
        try:
            print(f"Connecting to {remoteIp}:{remotePort}")
            self.remote = (remoteIp, remotePort)
            self.send("init")
            print(f"{self.context.name} ready")
        except socket.error as error:
            print(error)

def place_ships(board, health, name, number):
    dir_to_num = {'n': 0, 'e': 1, 's': 2, 'w': 3,
                  'N': 0, 'E': 1, 'S': 2, 'W': 3}
    letter_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
    system("Clear")
    position = input("Please type a coordinate for your " + name + " " + str(number) + ", for example A4: ")
    if health > 1:
        direction = input("Type a direction. (N: North, E: East, S: South, W: West): ")
    else:
        direction = 'S'

    any_ship = Ship((letter_to_num[position[0]] - 1, int(position[1]) - 1), dir_to_num[direction], health)
    if board.addShip(any_ship) is True:
        board.addShip(any_ship)
    else:
        print("Invalid coordinate(Overlap/Out of Map)")
        exit(1)

    board.displayDebug()
    time.sleep(2)


# handles incoming game move
def handleIncomingMove():

    print(f"Waiting for {remoteName}")
    # receive and process remote bomb
    bomb = server.receive()
    bombCoordinates = bomb.split(",")
    result = board.bomb(int(bombCoordinates[0]) - 1, int(bombCoordinates[1]) - 1)

    # send replies to remote player
    client.send(result)
    client.send(board.info())

    # stop if the game is over
    if board.isGameOver():
        print("Game over, you lose :-(")
        sys.exit()


# handles outgoing game move
def handleOutgoingMove():
    letter_to_num = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
                     'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10'}
    # send bomb to remote player
    bomb_ = input("Send bomb (e.G. A4): ")
    bomb = (letter_to_num[bomb_[0]] + "," + bomb_[1])
    # TODO: validate the input
    client.send(bomb)

    # receive and print replies from remote
    result = server.receive()
    print(result)
    boardInfo = server.receive()
    print(boardInfo)

    # stop if the game is over
    if "over" in result:
        print("Game over, you win!")
        sys.exit()


if __name__ == '__main__':
    # get app config
    # TODO: validate input arguments
    ip = "localhost"  # local host (or ip address)
    name = sys.argv[1]  # player name
    port = sys.argv[2]  # port
    if len(sys.argv) == 3:
        # first deployment, no remote connection info specified
        firstDeployment = True
    else:
        # second deployment
        firstDeployment = False

        # get remote connection info (ip address and port to connect to)
        remoteIp = sys.argv[3]
        remotePort = int(sys.argv[4])

    context = Context(ip, port, name)

    # initialize board
    print(f"Initialize board for {name}")
    board = Board(10, 10)

    if firstDeployment:
        # first deployment

        # Platziert die verschiedenen Schiffe mithilfe einer Abfrage vom User
        place_ships(board, 4, "Titanic", 1)
        place_ships(board, 3, "Cruiser", 1)
        place_ships(board, 3, "Cruiser", 2)
        place_ships(board, 2, "Yacht", 1)
        place_ships(board, 2, "Yacht", 2)
        place_ships(board, 2, "Yacht", 3)
        place_ships(board, 1, "Boat", 1)
        place_ships(board, 1, "Boat", 2)
        place_ships(board, 1, "Boat", 3)
        place_ships(board, 1, "Boat", 4)

        # initialize server
        server = Server(context)

        # wait for and handle initial incoming connection
        print(f"Waiting for player on {ip}:{port}")
        init = server.receive().split()
        remoteName = init[1]
        remoteIp = init[2]
        remotePort = int(init[3])
        print(f"{remoteName} connected")

        # trigger initial outgoing connection
        client = Client(context)
        client.init(remoteIp, remotePort)

        print("Starting game")

        # game loop
        while True:
            handleIncomingMove()
            handleOutgoingMove()

    else:
        # second deployment

        # TODO: get the ships from command line or config file and move after the board initialization
        place_ships(board, 4, "Titanic", 1)
        place_ships(board, 3, "Cruiser", 1)
        place_ships(board, 3, "Cruiser", 2)
        place_ships(board, 2, "Yacht", 1)
        place_ships(board, 2, "Yacht", 2)
        place_ships(board, 2, "Yacht", 3)
        place_ships(board, 1, "Boat", 1)
        place_ships(board, 1, "Boat", 2)
        place_ships(board, 1, "Boat", 3)
        place_ships(board, 1, "Boat", 4)

        # trigger initial outgoing connection
        client = Client(context)
        client.init(remoteIp, remotePort)

        # initialize server
        server = Server(context)

        # wait for and handle initial incoming connection
        print(f"Waiting for player on {ip}:{port}")
        init = server.receive().split()
        remoteName = init[1]
        print(f"{remoteName} connected")

        print("Starting game")

        # game loop
        while True:
            handleOutgoingMove()
            handleIncomingMove()
