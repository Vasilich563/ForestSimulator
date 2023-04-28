#Author Vodohleb04
class Hectare:

    def __init__(self, creations=None):
        if creations is None:
            creations = []
        self._creations = creations

    @property
    def creations(self):
        return self._creations

    def update_hectare(self, creations):
        self._creations = creations

    def extend_hectare(self, additional_creations):
        self._creations.extend(additional_creations)

class Forest:

    def __init__(self, vertical_length, horizontal_length):
        self._vertical_length = vertical_length
        self._horizontal_length = horizontal_length
        self._hectares = [[Hectare() for _ in range(horizontal_length)] for _ in range(vertical_length)]

    @property
    def hectares(self):
        return self._hectares

    @property
    def vertical_length(self):
        return self._vertical_length

    @property
    def horizontal_length(self):
        return self._horizontal_length
