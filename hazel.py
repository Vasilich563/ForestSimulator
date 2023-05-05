#Author Vodohleb04
import configs
from plant import Plant
import configs
from typing import List
import random


class Hazel(Plant):

    _life_median = configs.LifeMedian.HAZEL_LM.value
    _max_hp = configs.MaxHP.HAZEL_MHP.value
    _start_hp = configs.StartHP.HAZEL_START_HP.value
    _hp_reduction = configs.PlantHPReduction.HAZEL_HPR.value
    _offspring_dispersion = configs.PlantOffspringDispersion.HAZEL_OD.value
    _offspring_nutritional_value = configs.NutritionalValue.HAZEL_OFFSPRING_NV.value
    _start_shrub_nutritional_value = configs.NutritionalValue.START_HAZEL_SNV.value
    _shrub_reduction = configs.PlantShrubReduction.HAZEL_SR.value
    _reproduction_age_interval = configs.ReproductionAgeInterval.HAZEL_RAI.value
    _id_counter = 0

    @staticmethod
    def rewrite_id_counter(new_id_counter: int) -> None:
        """Sets new value for id_counter (no matter, what is a value of id_counter)"""
        if new_id_counter < 0:
            raise ValueError(f"New if counter {new_id_counter} must be >= 0")
        Hazel._id_counter = new_id_counter

    @staticmethod
    def set_id_counter(new_id_counter: int) -> None:
        """Sets new value for id_counter (can't set value that less than current value)"""
        if new_id_counter < Hazel._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >= than old id counter({Hazel._id_counter})")
        Hazel.rewrite_id_counter(new_id_counter)

    @staticmethod
    def get_id_counter() -> int:
        """Returns the value of id_counter"""
        return Hazel._id_counter

    def __init__(self, unpack_dict_flag=False, info_d=None):
        """Creates hazel

        unpack_dict_flag - True when needs to unpack creature from dict
        info_dict - dict with parameters of creature
        """
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Hazel._id_counter += 1
            return

        self._age = 0
        self._hp = self._start_hp
        self._nutritional_value = self._start_shrub_nutritional_value
        super()._make_power_coefficient(configs.PersonalPowerCoefficientParameters.HAZEL_PPCP)
        self._id = configs.IdPrefix.HAZEL_PREF.value + str(self._id_counter)
        Hazel._id_counter += 1

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        start_power = configs.StartPower.HAZEL_SP.value
        k_func_coefficient = configs.PowerFunctionCoefficient.HAZEL_PFC.value
        if self.age <= self._reproduction_age_interval[0]:  # Progression of power
            return self._power_coefficient * (start_power + (k_func_coefficient * self.age))
        else:  # Maximal power (const)
            return self._power_coefficient * (start_power + (k_func_coefficient * self._reproduction_age_interval[0]))

    def produce_eatable_offspring(self) -> None:
        min_amount, max_amount = configs.PlantEatableOffspringPossibleAmount.HAZEL_EOPA.value
        for i in range(random.randint(min_amount, max_amount)):
            self._nutritional_value += self._offspring_nutritional_value

    def reproduction(self) -> List:
        min_numb, max_numb = configs.ChanceToProduceKids.HAZEL_CTPK.value
        chance_to_produce = random.randint(min_numb, max_numb)
        if self._can_produce_children() and chance_to_produce == 1:
            min_amount, max_amount = configs.PossibleKidsAmount.HAZEL_PKA.value
            grown_amount = random.randint(min_amount, max_amount)
            return [Hazel() for _ in range(grown_amount)]
        return []

    def be_eaten(self, nutritional_value: int) -> int:
        if nutritional_value > self._nutritional_value:
            self._nutritional_value = 0
            self.get_hearted(int(0.5 * (nutritional_value - self._nutritional_value)))
        else:
            self._nutritional_value -= nutritional_value
            self.get_hearted(int(nutritional_value * configs.UnprotectedDamageMultiplier.HAZEL_UDM.value))
        return nutritional_value

    def stats(self) -> str:
        return "Kingdom: Plant" \
               "Kind: Hazel" + super().stats()
