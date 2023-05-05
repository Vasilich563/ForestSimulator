#Author Vodohleb04
from abc import ABC, abstractmethod
from typing import Tuple
from random import randint

from forest import Hectare
from configs import PersonalPowerCoefficientParameters


class Aging(ABC):

    # _age: int
    @property
    def age(self) -> int:
        """Returns age of creature"""
        return self._age

    @abstractmethod
    def live_time_cycle(self) -> None:
        """Creature makes its activities in live cycle"""
        raise NotImplementedError


class Dieable(ABC):

    # _life_median: int
    # _hp: int
    # _start_hp: int
    @property
    def hp(self) -> int:
        """Returns health points of creature"""
        return self._hp

    def get_hearted(self, damage: int) -> None:
        """Reduce health of creature after getting damaged"""
        if self._hp > damage:
            self._hp -= damage
        else:
            self.die()

    def is_dead(self) -> bool:
        """Checks if creature is dead"""
        return self._hp <= 0

    def die(self) -> None:
        """Kills creature"""
        if not self.is_dead():
            self._hp = 0

    def unexpected_death(self) -> None:
        """Random death of creature"""
        chance_to_die = randint(0, 100)
        if chance_to_die == 0:
            self.die()


class Eatable(ABC):

    # _nutritional_value: int
    @abstractmethod
    def be_eaten(self, nutritional_value) -> int:
        """Be eaten by another creature"""
        raise NotImplementedError


class Powerful(ABC):

    # _power_coefficient: float
    # _damage
    @abstractmethod
    def power(self) -> float:
        """Count power of this creature

        Power of creature defines who can eat this creature and who can be eaten by this creature
        Power works as passive protection (one creature can not eat the other one if the second one has more power)
        Power depends on multiple parameters:
            basic power - depends on type of creature
            personal power coefficient - minimal and maximal values depends on type of creature, can variate from
                creature to creature of the same type
            age of creature
        """
        raise NotImplementedError

    @staticmethod
    def __ppcp_parser(ppcp_of_class: PersonalPowerCoefficientParameters) -> Tuple[int, int, int]:
        """Sets values to count power coefficient for creature

        This values determines interval of personal power coefficient for type of creatures (depends on type)
        """
        if not isinstance(ppcp_of_class, PersonalPowerCoefficientParameters):
            raise TypeError
        min_numerator = ppcp_of_class.value["min_numerator"]
        max_numerator = ppcp_of_class.value["max_numerator"]
        denominator = ppcp_of_class.value["denominator"]
        return min_numerator, max_numerator, denominator

    def _make_power_coefficient(self, ppcp_of_class: PersonalPowerCoefficientParameters) -> None:
        """Sets personal power coefficient of creature

        Maximal and minimal power coefficient depends on type of creature but coefficient can variete from one creature
            to another
        """
        if not isinstance(ppcp_of_class, PersonalPowerCoefficientParameters):
            raise TypeError
        min_numerator, max_numerator, denominator = Powerful.__ppcp_parser(ppcp_of_class)
        self._power_coefficient = randint(min_numerator, max_numerator) / denominator

    @abstractmethod
    def protect(self, enemy) -> bool:
        """Protect from attack of other creature

        enemy - creature that tries to attack this creature

        returns True if creature protected itself successfully
        """
        raise NotImplementedError


class Movable(ABC):
    # Only for animals

    @abstractmethod
    def move(self, forest):
        """Change position of creature in forest

        forest: Forest - data container for creatures
        """
        raise NotImplementedError


class Hunger(ABC):
    # Only for animals

    @property
    def food_energy(self) -> None:
        """Returns value of food_energy of creature

        If creature is starving it may occur death
        """
        return self._food_energy

    def cycle_starvation(self) -> None:
        """Reduces food energy of creature

        Value of reducing food energy depends on type of creature
        """
        if self._food_energy > self._hunger_per_cycle:
            self._food_energy -= self._hunger_per_cycle
        else:
            self._food_energy = 0
            self.get_hearted(self._hunger_per_cycle / 5)

    @abstractmethod
    def search_for_food(self, hectare: Hectare):
        """Creature try to find food and eat it"""
        raise NotImplementedError

    @abstractmethod
    def _eat(self, eatable: Eatable):
        """Process of getting food from eatable

        eatable: creature that can be eaten by this creature
        """
        raise NotImplementedError
