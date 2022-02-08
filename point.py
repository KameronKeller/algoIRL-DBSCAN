from calendar import c


class Point:

    def __init__(self, coordinates = [], label = None):
        self.coordinates = coordinates
        self.label = label

    def coords(self):
        return self.coordinates

    def __repr__(self):
        return str(self.coordinates)

    def set_label(self, label):
        self.label = label