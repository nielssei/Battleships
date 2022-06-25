# Klasse initialisiert Schiffe
class Ship:
    def __init__(self, origin, direction, size):
        self.size = size
        # Koordinaten werden hier gespeichert:
        self.coordinates = []
        # Ursprungskoordinate wird um so viele Koordinaten erweitert, wie groß das Schiff ist
        # in die ausgewählte Richtung. (0: Norden, 1: Osten, 2: Süden, 3: Westen)
        for k in range(size):
            if direction == 0:
                self.coordinates.append((origin[0] - k, origin[1]))
            if direction == 1:
                self.coordinates.append((origin[0], origin[1] + k))
            if direction == 2:
                self.coordinates.append((origin[0] + k, origin[1]))
            if direction == 3:
                self.coordinates.append((origin[0], origin[1] - k))
            
