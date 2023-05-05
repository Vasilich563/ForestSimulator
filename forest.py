#Author Vodohleb04
from typing import List


class Hectare:

    def __init__(self, creations=None):
        """Creates hectare

        creations - creations to add to hectare, if None - creates empty Hectare
        Minimal data container of program - emplace creatures
        """
        if creations is None:
            creations = []
        self._creations = creations

    @property
    def creations(self) -> List:
        """Returns list of creation, located in hectare"""
        return self._creations

    def update_hectare(self, creations) -> None:
        """Emplace new creations instead of already located there"""
        self._creations = creations

    def extend_hectare(self, additional_creations) -> None:
        """Add new creatures to hectare without removing the of old one"""
        self._creations.extend(additional_creations)


class Forest:

    def __init__(self, vertical_length, horizontal_length):
        """Creates forest

        vertical_length - amount of hectares lines (amount of hectares in vertical orientation)
        horizontal_length - amount of hectares columns (amount of hectares in horizontal orientation)
        Main data container of program. Presented as matrix MxN size
            N = vertical_length
            M = horizontal_length
            Every part of matrix is a Hectare. All manipulations implemented in EcoSystem. All data saved in this class.
        """
        self._vertical_length = vertical_length
        self._horizontal_length = horizontal_length
        self._hectares = [[Hectare() for _ in range(horizontal_length)] for _ in range(vertical_length)]

    @property
    def hectares(self) -> List[List[Hectare]]:
        """Returns matrix with Hectares"""
        return self._hectares

    @property
    def vertical_length(self) -> int:
        """Returns amount of string in matrix (amount of Hectares in vertical orientation)"""
        return self._vertical_length

    @property
    def horizontal_length(self) -> int:
        """Returns amount of columns in matrix (amount of Hectares in horizontal orientation)"""
        return self._horizontal_length
