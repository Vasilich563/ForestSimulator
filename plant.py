#Author Vodohleb04
from creature_interfaces import Dieable, Aging, Eatable, Powerful
from reproduction import NonGenderReproduction
from abc import ABC
from typing import Tuple
from random import randint



class Plant(Dieable, Aging, NonGenderReproduction, Eatable, Powerful, ABC):

    # _hp_reduction: int
    # _shrub_reduction: int
    # _basic_shrub_nutritional_value: int
    # _offspring_nutritional_value: int
    # _offspring_dispersion: int

    def _can_produce_children(self) -> bool:
        return self._reproduction_age_interval[0] <= self.age <= self._reproduction_age_interval[1] and\
            not self.is_dead()

    def produce_eatable_offspring(self) -> None:
        """Produce eatable offsprings that just increase nutritional value of creature but don't become new creatures"""
        raise NotImplementedError

    def regenerate(self) -> None:
        """Regenerates plant\'s health points"""
        if not self.is_dead() and self.hp < self._max_hp:
            self._hp += self._hp_reduction
            if self._hp > self._max_hp:
                self._hp = self._max_hp
            self._nutritional_value += self._shrub_reduction

    def die(self) -> None:
        if not self.is_dead():
            self._id += "_dead"
            super().die()

    @property
    def offspring_dispersion(self) -> int:
        return self._offspring_dispersion

    def live_time_cycle(self) -> None:
        self._age += 1

        if self._age > self._life_median:
            chance = randint(0, self._age - self._life_median)
            if chance != 0:
                self.die()
                return
        self.unexpected_death()

        self.regenerate()

    def protect(self, enemy) -> bool:
        """No active protection"""
        return False  # Can't protect

    def get_dict_of_info(self) -> dict:
        """Returns dict with parameters of creature

        This method is used to save creature in json file
        """
        return {
            "age": self._age,
            "hp": self._hp,
            "nutritional_value": self._nutritional_value,
            "power_coefficient": self._power_coefficient,
            "id": self._id
        }

    def _unpack_info_from_dict(self, info: dict):
        """Sets creature parameters from Dict

        info - Dict with parameters of creature
        """
        self._age = info["age"]
        self._hp = info["hp"]
        self._nutritional_value = info["nutritional_value"]
        self._power_coefficient = info["power_coefficient"]
        self._id = info["id"]

    def stats(self) -> str:
        """Returns string with information about creature conditions

        Useful in console application
        """
        life_status = "Dead" if self.is_dead() else f"HP: {self.hp}\n Power: {self.power()}"
        reproductive = "Can" if self.reproduction_age_interval[0] <= self.age <= self.reproduction_age_interval[1] \
            else "Can't"
        return f" ID: {self.id}" \
               f"{life_status}" \
               f"Age: {self.age}" \
               f"Nutritional Value: {self._nutritional_value}" \
               f"{reproductive} produce kids."
