#Author Vodohleb04
from abc import ABC, abstractmethod
from typing import Tuple

import configs
from forest import Hectare
from configs import Genders
import random


class Reproduction(ABC):

    #_reproduction_age_interval: Tuple[int, int]
    #_id: str
    #_id_counter: int

    def __str__(self):
        return f"{self.id}"

    @property
    def id(self):
        return self._id

    @property
    def reproduction_age_interval(self) -> Tuple[int, int]:
        return self._reproduction_age_interval


class NonGenderReproduction(Reproduction, ABC):

    @property
    @abstractmethod
    def offspring_dispersion(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def _can_produce_children(self) -> bool:
        raise NotImplementedError

    def is_reproductive(self) -> bool:
        return self._can_produce_children()

    @abstractmethod
    def reproduction(self):
        raise NotImplementedError


class GenderReproduction(Reproduction, ABC):

    #_gender: Genders
    #_parents: Tuple[str, str]

    @property
    def gender(self) -> Genders:
        return self._gender

    @property
    def parents(self) -> Tuple[str, str]:
        return self._parents

    def _are_relatives(self, possible_relative) -> bool:
        if possible_relative.id in self.parents or self.id in possible_relative.parents:
            return True
        if configs.CREATOR in self.parents or configs.CREATOR in possible_relative.parents:
            return False
        if self.parents[0] in possible_relative.parents or self.parents[1] in possible_relative.parents:
            return True
        return False

    @property
    def father(self) -> str:
        if self.parents[0].startswith(Genders.MALE.value):
            return self.parents[0]
        else:
            return self.parents[1]

    @property
    def mother(self) -> str:
        if self.parents[0].startswith(Genders.FEMALE.value):
            return self.parents[0]
        else:
            return self.parents[1]

    @abstractmethod
    def _can_produce_children(self, partner) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_reproductive(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def _produce_children(self, partner):
        raise NotImplementedError
    
    @abstractmethod
    def _search_for_partner(self, hectare: Hectare):
        raise NotImplementedError

    def reproduction(self, hectare: Hectare):
        if not isinstance(hectare, Hectare):
            raise TypeError
        return self._produce_children(self._search_for_partner(hectare))

    @staticmethod
    def _random_gender() -> Genders:
        gender_chance = random.randint(0, 9)
        if gender_chance % 2 == 0:
            return Genders.FEMALE
        else:
            return Genders.MALE
