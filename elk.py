#Author Vodohleb04
import random
from typing import List
import configs
from animal_types_interfaces import Herbivore
from forest import Hectare


class Elk(Herbivore):

    _life_median = configs.LifeMedian.ELK_LM.value
    _reproduction_age_interval = configs.ReproductionAgeInterval.ELK_RAI.value
    _id_counter = 0
    _hunger_per_cycle = configs.HungerPerCycle.ELK_HPC.value
    _required_nutritional_value = configs.RequiredNutritionalValue.ELK_RNV.value

    @staticmethod
    def rewrite_id_counter(new_id_counter: int) -> None:
        """Sets new value for id_counter (no matter, what is a value of id_counter)"""
        if new_id_counter < 0:
            raise ValueError(f"New if counter {new_id_counter} must be >= 0")
        Elk._id_counter = new_id_counter

    @staticmethod
    def set_id_counter(new_id_counter: int) -> None:
        """Sets new value for id_counter (can't set value that less than current value)"""
        if new_id_counter < Elk._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >= than old id counter({Elk._id_counter})")
        Elk.rewrite_id_counter(new_id_counter)

    @staticmethod
    def get_id_counter() -> int:
        """Returns the value of id_counter"""
        return Elk._id_counter

    def __init__(self, mother_name=configs.CREATOR, father_name=configs.CREATOR, unpack_dict_flag=False, info_d=None):
        """Creates elk

        mother_name - id of mother (default - CREATOR from config)
        father_name - id of mother (default - CREATOR from config)
        unpack_dict_flag - True when needs to unpack creature from dict
        info_dict - dict with parameters of creature
        """
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Elk._id_counter += 1
            return

        self._gender = super()._random_gender()
        if self._gender == configs.Genders.MALE:
            ppcp_by_gender = configs.PersonalPowerCoefficientParameters.M_ELK_PPCP
        else:
            ppcp_by_gender = configs.PersonalPowerCoefficientParameters.FEM_ELK_PPCP
        super()._make_power_coefficient(ppcp_by_gender)
        self._damage = configs.Damage.ELK_D.value * self._power_coefficient
        self._age = 0
        self._hp = configs.MaxHP.ELK_MHP.value
        self._nutritional_value = configs.NutritionalValue.ELK_NV.value
        self._food_energy = self._hunger_per_cycle * 2
        self._id = self._gender.value + "_" + configs.IdPrefix.ELK_PREF.value + "_" + str(self._id_counter)
        Elk._id_counter += 1
        self._sterile_period = self._reproduction_age_interval[0]
        self._parents = (mother_name, father_name)

    def _produce_children(self, partner) -> List:
        if partner:
            min_numb, max_numb = configs.ChanceToProduceKids.ELK_CTPK.value
            chance_to_produce = random.randint(min_numb, max_numb)
            if chance_to_produce == 1:
                min_amount, max_amount = configs.PossibleKidsAmount.ELK_PKA.value
                kids_amount = random.randint(min_amount, max_amount)
                self._sterile_period = configs.SterilePeriods.ELK_SP.value
                partner._sterile_period = configs.SterilePeriods.ELK_SP.value
                mother_name = self.id if self.gender == configs.Genders.FEMALE else partner.id
                father_name = self.id if self.gender == configs.Genders.MALE else partner.id
                return [Elk(mother_name=mother_name, father_name=father_name) for _ in range(kids_amount)]
        return []

    def _can_produce_children(self, partner) -> bool:
        if isinstance(self, Elk) and isinstance(partner, Elk):
            return super()._can_produce_children(partner)
        else:
            return False

    def _search_for_partner(self, hectare: Hectare):
        if not isinstance(hectare, Hectare):
            raise TypeError
        for possible_partner in hectare.creations:
            if isinstance(possible_partner, Elk) and self._can_produce_children(possible_partner):
                return possible_partner
        return None

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        if self._gender == configs.Genders.MALE:
            start_power = configs.StartPower.M_ELK_SP.value
            k_func_coefficient = configs.PowerFunctionCoefficient.M_ELK_PFC.value
        else:
            start_power = configs.StartPower.FEM_ELK_SP.value
            k_func_coefficient = configs.PowerFunctionCoefficient.FEM_ELK_PFC.value

        if self.age <= self._reproduction_age_interval[0]:  # Progression of power
            return self._power_coefficient * (start_power + (k_func_coefficient * self.age))
        elif self.age <= self._reproduction_age_interval[1]:  # Maximal power (const)
            return self._power_coefficient * (start_power + (k_func_coefficient * self._reproduction_age_interval[0]))
        else:  # Regression of power
            return self._power_coefficient * (start_power + (-k_func_coefficient * self._reproduction_age_interval[0]))

    def stats(self) -> str:
        return " Kingdom: Animal" \
               "Type: Herbivore" \
               "Kind: Elk" + super().stats()
