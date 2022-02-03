from calendar import c


class Point:

    def __init__(self, coordinates = []):
        self.coordinates = coordinates

    def coords(self):
        return self.coordinates

    def __repr__(self):
        return str(self.coordinates) 