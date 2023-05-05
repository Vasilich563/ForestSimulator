#Author Vodohleb04
import random
from abc import ABC
from typing import Tuple, Dict
from creature_interfaces import Movable, Dieable, Aging, Eatable, Hunger, Powerful
from reproduction import GenderReproduction
from random import randint
from forest import Forest
import configs


class Animal(Movable, Dieable, Aging, Eatable, GenderReproduction, Hunger, Powerful, ABC):

    #_sterile_period: int

    def be_eaten(self, nutritional_value: int) -> int:
        """Reduce nutritional value of creature if it is eaten (returns reduced value)

        nutritional_value - amount, that other creature want to eat
        """
        if self._nutritional_value > nutritional_value:
            self._nutritional_value -= nutritional_value
            return nutritional_value
        else:
            self._nutritional_value = 0
            return nutritional_value

    def die(self) -> None:
        """Makes creature dead"""
        if not self.is_dead():
            self._hunger_per_cycle = 0
            self._id += "_dead"
            super().die()

    def protect(self, enemy) -> bool:
        """Try to protect from attack of other creature

        enemy: Animal - creature, that tries to attack this creature
        return bool - True, if creature protect itself successfully
        """
        lucky_chance = randint(0, 1)
        if lucky_chance == 1:
            enemy.get_hearted(self._damage)
            self.get_hearted(enemy._damage * configs.UnprotectedDamageMultiplier.EVERY_ANIMAL_UDM.value)
            return True
        else:
            return False

    def _can_produce_children(self, partner) -> bool:
        """Determines if creature can produce children with partner

        partner: Animal of the same type
        return True, if creatures can produce children
        """
        if self.is_dead() or partner.is_dead():
            return False
        elif self.gender == partner.gender:
            return False
        elif not self._reproduction_age_interval[0] <= self.age <= self._reproduction_age_interval[1]:
            return False
        elif not partner._reproduction_age_interval[0] <= partner.age <= partner._reproduction_age_interval[1]:
            return False
        elif self._sterile_period > 0 or partner._sterile_period > 0:
            return False
        elif self._are_relatives(partner):
            return False
        else:
            return True

    def is_reproductive(self) -> bool:
        """Determines if creature is ready to produce children

        return True if creature is ready to produce children
        """
        if self.is_dead():
            return False
        elif not self._reproduction_age_interval[0] <= self.age <= self._reproduction_age_interval[1]:
            return False
        elif self._sterile_period > 0:
            return False
        else:
            return True

    def live_time_cycle(self) -> None:
        """Makes time cycle activities of creature"""
        self._age += 1
        self._sterile_period -= 1

        if self._age > self._life_median:
            chance = randint(0, self._age - self._life_median)
            if chance != 0:
                self.die()
                return
        self.unexpected_death()
        # TODO Search for food, chance to move in class Forest

    def __find_position_in_forest(self, forest: Forest) -> Tuple[int, int]:
        """Determines position of creature in forest

        forest - data container for creatures
        return Tuple[int, int] - vertical index of creature, horizontal index of creature
        """
        not_found_flag = True
        i = 0
        j = 0
        for hectare_line in forest.hectares:
            j = 0
            for hectare in hectare_line:
                if self in hectare.creations:
                    not_found_flag = False
                    break
                j += 1
            else:
                i += 1
                continue
            break
        if not_found_flag:
            raise ValueError(f"Creature with id {self.id} wasn't found in forest")
        return i, j

    def move(self, forest: Forest) -> None:
        """Move this creature to another hectare of forest

        forest - data container for creatures
        """
        chance_to_move = randint(1, 3)
        if chance_to_move != 1:
            return
        if not isinstance(forest, Forest):
            raise TypeError
        vertical_pos, horizontal_pos = self.__find_position_in_forest(forest)
        vertical_shift = random.randint(-1, 1)
        horizontal_shift = random.randint(-1, 1)
        while vertical_shift == 0 or\
                horizontal_shift == 0 or\
                vertical_pos + vertical_shift >= forest.vertical_length or\
                horizontal_pos + horizontal_shift >= forest.horizontal_length:
            vertical_shift = random.randint(-1, 1)
            horizontal_shift = random.randint(-1, 1)
        forest.hectares[vertical_pos][horizontal_pos].creations.remove(self)
        forest.hectares[vertical_pos + vertical_shift][horizontal_pos + horizontal_shift].creations.append(self)

    def get_dict_of_info(self) -> dict:
        """Returns dict with parameters of creature

        This method is used to save creature in json file
        """
        return {
            "gender": self.gender.value,
            "power_coefficient": self._power_coefficient,
            "damage": self._damage,
            "age": self._age,
            "hp": self._hp,
            "nutritional_value": self._nutritional_value,
            "food_energy": self._food_energy,
            "id": self._id,
            "sterile_period": self._sterile_period,
            "parents": self._parents
        }

    def _unpack_info_from_dict(self, info: Dict):
        """Sets creature parameters from Dict

        info - Dict with parameters of creature
        """
        self._gender = configs.Genders.MALE if info["gender"] == "male" else configs.Genders.FEMALE
        self._power_coefficient = info["power_coefficient"]
        self._damage = info["damage"]
        self._age = info["age"]
        self._hp = info["hp"]
        self._nutritional_value = info["nutritional_value"]
        self._food_energy = info["food_energy"]
        self._id = info["id"]
        self._sterile_period = info["sterile_period"]
        self._parents = info["parents"]

    def stats(self) -> str:
        """Returns string with information about creature conditions

        Useful in console application
        """
        life_status = "Dead" if self.is_dead() else f"HP: {self.hp}\n Power: {self.power()}"
        reproductive = "Can" if self._sterile_period <= 0 and \
            self.reproduction_age_interval[0] <= self.age <= self.reproduction_age_interval[1] else "Can't"
        return f" ID: {self.id}\n" \
               f"{life_status}\n" \
               f"Age: {self.age}\n" \
               f"Gender: {self._gender}\n" \
               f"Food energy: {self._food_energy}\n" \
               f"Nutritional Value: {self._nutritional_value}\n" \
               f"Mother: {self.parents[0]}. Father: {self.parents[1]}\n" \
               f"{reproductive} produce kids."
