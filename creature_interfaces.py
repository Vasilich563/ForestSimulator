#Author Vodohleb04
from abc import ABC, abstractmethod
from typing import NoReturn, Tuple
from random import randint

from forest import Hectare
from configs import PersonalPowerCoefficientParameters


class Aging(ABC):

    # _age: int
    @property
    def age(self) -> int:
        return self._age

    @abstractmethod
    def live_time_cycle(self) -> NoReturn:
        raise NotImplementedError


class Dieable(ABC):

    # _life_median: int
    # _hp: int
    # _start_hp: int
    @property
    def hp(self) -> int:
        return self._hp

    def get_hearted(self, damage: int) -> NoReturn:
        if self._hp > damage:
            self._hp -= damage
        else:
            self.die()

    def is_dead(self) -> bool:
        return self._hp <= 0

    def die(self) -> NoReturn:
        if not self.is_dead():
            self._hp = 0

    def unexpected_death(self) -> NoReturn:
        chance_to_die = randint(0, 100)
        if chance_to_die == 0:
            self.die()


class Eatable(ABC):

    # _nutritional_value: int
    @abstractmethod
    def be_eaten(self, nutritional_value) -> int:
        raise NotImplementedError


class Powerful(ABC):

    # _power_coefficient: float
    # _damage
    @abstractmethod
    def power(self) -> float:
        raise NotImplementedError

    @staticmethod
    def __ppcp_parser(ppcp_of_class: PersonalPowerCoefficientParameters) -> Tuple[int, int, int]:
        if not isinstance(ppcp_of_class, PersonalPowerCoefficientParameters):
            raise TypeError
        min_numerator = ppcp_of_class.value["min_numerator"]
        max_numerator = ppcp_of_class.value["max_numerator"]
        denominator = ppcp_of_class.value["denominator"]
        return min_numerator, max_numerator, denominator

    def _make_power_coefficient(self, ppcp_of_class: PersonalPowerCoefficientParameters) -> NoReturn:
        if not isinstance(ppcp_of_class, PersonalPowerCoefficientParameters):
            raise TypeError
        min_numerator, max_numerator, denominator = Powerful.__ppcp_parser(ppcp_of_class)
        self._power_coefficient = randint(min_numerator, max_numerator) / denominator

    @abstractmethod
    def protect(self, enemy) -> bool:
        raise NotImplementedError


class Movable(ABC):
    # Only for animals

    @abstractmethod
    def move(self, forest):
        raise NotImplementedError


class Hunger(ABC):
    # Only for animals

    @property
    def food_energy(self) -> NoReturn:
        return self._food_energy

    def cycle_starvation(self) -> NoReturn:
        if self._food_energy > self._hunger_per_cycle:
            self._food_energy -= self._hunger_per_cycle
        else:
            self._food_energy = 0
            self.get_hearted(self._hunger_per_cycle / 5)

    @abstractmethod
    def search_for_food(self, hectare: Hectare):
        raise NotImplementedError

    @abstractmethod
    def _eat(self, eatable: Eatable):
        raise NotImplementedError
