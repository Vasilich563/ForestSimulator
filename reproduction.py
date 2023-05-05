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

    def __str__(self) -> str:
        return f"{self.id}"

    @property
    def id(self) -> str:
        """Returns identificator of creature

        Every creature has its own unique identificator
        For creatures with non-gender reproduction is *creature-type*_*id-number*
            creature-type - name of creature type
            id-number - unique identificator number (unique in within class)
        For creatures with gender reproduction is *gender*_*creature-type*_*id-number*
            gender - gender of creature (determines randomly in __init__ of creature)
            creature-type - name of creature type
            id-number - unique identificator number (unique in within class)
        """
        return self._id

    @property
    def reproduction_age_interval(self) -> Tuple[int, int]:
        """Returns interval of reproduction age for this creature"""
        return self._reproduction_age_interval


class NonGenderReproduction(Reproduction, ABC):

    @property
    @abstractmethod
    def offspring_dispersion(self) -> int:
        """Returns maximal dispersion of offsprings for this creature"""
        raise NotImplementedError

    @abstractmethod
    def _can_produce_children(self) -> bool:
        """Determines if creature can produce children (offsprings)"""
        raise NotImplementedError

    def is_reproductive(self) -> bool:
        """Determines if creature is reproductive"""
        return self._can_produce_children()

    @abstractmethod
    def reproduction(self):
        """Makes children (offspring) of creature and disperse them"""
        raise NotImplementedError


class GenderReproduction(Reproduction, ABC):

    #_gender: Genders
    #_parents: Tuple[str, str]

    @property
    def gender(self) -> Genders:
        """Returns gender of creature"""
        return self._gender

    @property
    def parents(self) -> Tuple[str, str]:
        """Returns identificators of creatures\'s parents """
        return self._parents

    def _are_relatives(self, possible_relative) -> bool:
        """Defines if creatures are relatives"""
        if possible_relative.id in self.parents or self.id in possible_relative.parents:
            return True
        if configs.CREATOR in self.parents or configs.CREATOR in possible_relative.parents:
            return False
        if self.parents[0] in possible_relative.parents or self.parents[1] in possible_relative.parents:
            return True
        return False

    @property
    def father(self) -> str:
        """Returns identificator of creature\'s father"""
        if self.parents[0].startswith(Genders.MALE.value):
            return self.parents[0]
        else:
            return self.parents[1]

    @property
    def mother(self) -> str:
        """Returns identificator of creature\'s mother"""
        if self.parents[0].startswith(Genders.FEMALE.value):
            return self.parents[0]
        else:
            return self.parents[1]

    @abstractmethod
    def _can_produce_children(self, partner) -> bool:
        """Determines if creature can produce children with partner

        partner - other creature of this type to produce children with
        """
        raise NotImplementedError

    @abstractmethod
    def is_reproductive(self) -> bool:
        """Determines if creature reproductive (can produce children generally)"""
        raise NotImplementedError

    @abstractmethod
    def _produce_children(self, partner):
        """Makes children with partner

        partner - other creature of the same type of creatures to produce children
        """
        raise NotImplementedError
    
    @abstractmethod
    def _search_for_partner(self, hectare: Hectare):
        """Search for partner to produce children in hectare"""
        raise NotImplementedError

    def reproduction(self, hectare: Hectare):
        """Process of searching for partner and producing children"""
        if not isinstance(hectare, Hectare):
            raise TypeError
        return self._produce_children(self._search_for_partner(hectare))

    @staticmethod
    def _random_gender() -> Genders:
        """Returns random gender"""
        gender_chance = random.randint(0, 9)
        if gender_chance % 2 == 0:
            return Genders.FEMALE
        else:
            return Genders.MALE
