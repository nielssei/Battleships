import socket
import sys

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
        # Socket wird erstellt
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((str(self.context.ip), int(self.context.port)))
        self.socket.listen()

        (conn, addr) = self.socket.accept()

        # Nachricht über Socket erhalten
        data = conn.recv(500)
        message = data.decode()

        # Antwort
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

        # Verbindung erstellen
        if message.startswith("init"):
            message = message + " " + self.context.name + " " + self.socket.getsockname()[0] + " " + self.context.port

        self.socket.sendall(message.encode())

        self.socket.close()

    # Schickt Anfrage zur Verbindung
    def init(self, remote_ip, remote_port):
        try:
            print(f"Connecting to {remote_ip}:{remote_port}")
            self.remote = (remote_ip, remote_port)
            self.send("init")
            print(f"{self.context.name} ready")
        except socket.error as error:
            print(error)

def place_ships(board, health, name, number):
    # Nimmt Input vom User, um Schiffe zu platzieren
    dir_to_num = {'n': 0, 'e': 1, 's': 2, 'w': 3,
                  'N': 0, 'E': 1, 'S': 2, 'W': 3}
    letter_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
    position = input("Please type a coordinate for your " + name + " " + str(number) + ", for example A4: ")
    # Falls es sich um ein 1-Feld-Schiff handelt, ist die Richtung egal
    if health > 1:
        direction = input("Type a direction. (N: North, E: East, S: South, W: West): ")
    else:
        direction = 'S'
    # Koordinaten werden hinzugefügt und Schiff wird platziert, wenn alle Bedingungen aus add_ship zutreffen
    any_ship = Ship((letter_to_num[position[0]] - 1, int(position[1]) - 1), dir_to_num[direction], health)
    if board.add_ship(any_ship) is True:
        board.add_ship(any_ship)
    else:
        print("Invalid coordinate(Overlap/Out of Map)")
        exit(1)

    board.display_all()


# Methode, um mit eingehenden Angriffen umzugehen
def handle_incoming_move():

    print(f"Waiting for {remote_name}")
    # Eingehenden Angriff verarbeiten, auswerten
    bomb = server.receive()
    bomb_coordinates = bomb.split(",")
    result = board.bomb(int(bomb_coordinates[0]) - 1, int(bomb_coordinates[1]) - 1)

    # Antwort mit entsprechendem Ergebnis des Angriffs wird zurückgeschickt
    client.send(result)
    client.send(board.info())

    # Falls "Game Over" ist, wird eine Nachricht ausgegeben und das Spiel beendet
    if board.game_over():
        print("Game over, you lose :-(")
        sys.exit()


# Methode, um Angriffe zu senden
def handle_outgoing_move():
    letter_to_num = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
                     'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10'}
    # Anzugreifende Koordinate wird eingegeben
    bomb_ = input("Send bomb (e.G. A4): ")
    # Es wird überprüft, ob sie auf dem Spielfeld ist, wenn ja, wird sie formatiert und gesendet
    if 0 <= int(letter_to_num[bomb_[0]]) < 10 and 0 <= int(bomb_[1]) < 10:
        bomb = (letter_to_num[bomb_[0]] + "," + bomb_[1])
        client.send(bomb)
    else:
        print("Invalid Coordinate (OUT OF MAP)")

    # Angriffskoordinaten des Gegners erhalten und Ergebnis ausgeben
    result = server.receive()
    print(result)
    board_info = server.receive()
    print(board_info)

    # Exit, falls Spiel vorbei ist
    if "Over" in result:
        print("Game over, you win!")
        sys.exit()


if __name__ == '__main__':
    # Sockets werden konfiguriert und teilweise über Terminaleingabe festgelegt
    ip = "localhost"  # localhost / gewünschte IP
    name = sys.argv[1]  # Spielername
    port = sys.argv[2]  # Port
    if len(sys.argv) == 3:
        # Wenn es sich um "Spieler 1" handelt, sprich first deployment
        first_deployment = True
    else:
        # "Spieler 2", sprich second deployment
        first_deployment = False

        # Wenn "Spieler 2" sich verbindet, muss er IP und Port des Gegners eingeben
        remote_ip = sys.argv[3]
        remote_port = int(sys.argv[4])

    context = Context(ip, port, name)

    # Spielfeld wird initialisiert
    print(f"Initialize board for {name}")
    board = Board(10, 10)

    if first_deployment:
        print("Place your Ships. You have 4 different types of ships:"
              "\n"
              "\n- Titanic. 4 units long. 1 available."
              "\n- Cruiser. 3 units long. 2 available."
              "\n- Yacht. 2 units long. 3 available"
              "\n- Boat. 1 unit long. 4 available. \n")

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

        # Server wird initialisiert
        server = Server(context)

        # Auf Gegner warten / sich verbinden
        print(f"Waiting for player on {ip}:{port}")
        init = server.receive().split()
        remote_name = init[1]
        remote_ip = init[2]
        remote_port = int(init[3])
        print(f"{remote_name} connected")

        # Verbindung wird getriggert
        client = Client(context)
        client.init(remote_ip, remote_port)

        print("Starting game")

        # Game Loop, Spieler spielen abwechselnd
        while True:
            handle_incoming_move()
            handle_outgoing_move()

    else:
        print("Place your Ships. You have 4 different types of ships:"
              "\n"
              "\n- Titanic. 4 units long. 1 available."
              "\n- Cruiser. 3 units long. 2 available."
              "\n- Yacht. 2 units long. 3 available"
              "\n- Boat. 1 unit long. 4 available. \n")

        # "Spieler 2" Konfiguration Schiffe
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

        # Verbindung wird getriggert
        client = Client(context)
        client.init(remote_ip, remote_port)

        # Server wird initialisiert
        server = Server(context)

        # Auf Verbindung warten / sich verbinden
        print(f"Waiting for player on {ip}:{port}")
        init = server.receive().split()
        remote_name = init[1]
        print(f"{remote_name} connected")

        print("Starting game")

        # Game Loop, Spieler spielen abwechselnd
        while True:
            handle_outgoing_move()
            handle_incoming_move()


