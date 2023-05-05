#Author Vodohleb04
from abc import ABC
from animal import Animal
from plant import Plant
from typing import List
from forest import Hectare
import random


class Herbivore(Animal, ABC):

    #_required_nutritional_value: int

    def _eat(self, eatable: Plant) -> bool:
        """Eat some plant

        eatable - plant to eat
        """
        if isinstance(eatable, Plant):
            if eatable.power() <= self.power():
                self._food_energy += eatable.be_eaten(self._required_nutritional_value)
                return True
        return False

    def _count_amount_of_eatable_plants(self, creations: List) -> int:
        """Count amount of eatable plants in creations"""
        amount_of_plants = 0
        for creation in creations:
            if isinstance(creation, Plant) and creation.power() <= self.power():
                amount_of_plants += 1
        return amount_of_plants

    def search_for_food(self, hectare: Hectare) -> None:
        """Determines amount of plants to eat and eat it"""
        if not isinstance(hectare, Hectare):
            raise TypeError
        if not self.is_dead():
            if self._count_amount_of_eatable_plants(hectare.creations) > 0:
                amount_of_eaten = random.randint(1, self._count_amount_of_eatable_plants(hectare.creations))
                eaten_counter = 0
                while eaten_counter < amount_of_eaten:
                    if Herbivore._eat(self, random.choice(hectare.creations)):
                        eaten_counter += 1


class Predator(Animal, ABC):

    def _eat(self, eatable: Animal) -> bool:
        """Eat some animal"""
        if isinstance(eatable, Animal) and not isinstance(eatable, type(self)):
            if eatable.power() <= self.power():
                if not eatable.protect(self):
                    eatable.die()
                    self._food_energy += eatable.be_eaten(eatable._nutritional_value)
                return True
        return False

    def _count_amount_of_eatable(self, creations: List) -> int:
        """Counts amount of eatable animals in creations"""
        amount_of_eatable = 0
        for entity in creations:
            if isinstance(entity, Animal) and entity.power() <= self.power() and not isinstance(entity, type(self)):
                amount_of_eatable += 1
        return amount_of_eatable

    def search_for_food(self, hectare: Hectare) -> None:
        """Find eatable animal in hectare and eat it"""
        if not isinstance(hectare, Hectare):
            raise TypeError
        if not self.is_dead():
            if self._count_amount_of_eatable(hectare.creations) > 0:
                while not Predator._eat(self, random.choice(hectare.creations)):
                    continue


class Omnivorous(Predator, Herbivore, ABC):

    def search_for_food(self, hectare: Hectare) -> None:
        """Determines type of, and search for it and eat it"""
        if not isinstance(hectare, Hectare):
            raise TypeError
        food_choice = random.randint(1, 4)
        if food_choice == 1:
            Predator.search_for_food(self, hectare)
        else:
            Herbivore.search_for_food(self, hectare)
