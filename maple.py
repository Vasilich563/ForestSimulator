#Author Vodohleb04
from plant import Plant
import configs
from typing import List
import random


class Maple(Plant):

    _life_median = configs.LifeMedian.MAPLE_LM.value
    _max_hp = configs.MaxHP.MAPLE_MHP.value
    _start_hp = configs.StartHP.MAPLE_START_HP.value
    _hp_reduction = configs.PlantHPReduction.MAPLE_HPR.value
    _offspring_dispersion = configs.PlantOffspringDispersion.MAPLE_OD.value
    _offspring_nutritional_value = configs.NutritionalValue.MAPLE_OFFSPRING_NV.value
    _start_shrub_nutritional_value = configs.NutritionalValue.START_MAPLE_SNV.value
    _shrub_reduction = configs.PlantShrubReduction.MAPLE_SR.value
    _reproduction_age_interval = configs.ReproductionAgeInterval.MAPLE_RAI.value
    _id_counter = 0

    @staticmethod
    def rewrite_id_counter(new_id_counter: int) -> None:
        """Sets new value for id_counter (no matter, what is a value of id_counter)"""
        if new_id_counter < 0:
            raise ValueError(f"New if counter {new_id_counter} must be >= 0")
        Maple._id_counter = new_id_counter

    @staticmethod
    def set_id_counter(new_id_counter: int) -> None:
        """Sets new value for id_counter (can't set value that less than current value)"""
        if new_id_counter < Maple._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >= than old id counter({Maple._id_counter})")
        Maple.rewrite_id_counter(new_id_counter)

    @staticmethod
    def get_id_counter() -> int:
        """Returns the value of id_counter"""
        return Maple._id_counter

    def __init__(self, unpack_dict_flag=False, info_d=None):
        """Creates maple

        unpack_dict_flag - True when needs to unpack creature from dict
        info_dict - dict with parameters of creature
        """
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Maple._id_counter += 1
            return
        self._age = 0
        self._hp = self._start_hp
        self._nutritional_value = self._start_shrub_nutritional_value
        super()._make_power_coefficient(configs.PersonalPowerCoefficientParameters.MAPLE_PPCP)
        self._id = configs.IdPrefix.MAPLE_PREF.value + str(self._id_counter)
        Maple._id_counter += 1

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        start_power = configs.StartPower.MAPLE_SP.value
        k_func_coefficient = configs.PowerFunctionCoefficient.HAZEL_PFC.value
        if self.age <= self._reproduction_age_interval[0]:  # Progression of power
            return self._power_coefficient * (start_power + (k_func_coefficient * self.age))
        else:  # Maximal power (const)
            return self._power_coefficient * (start_power + (k_func_coefficient * self._reproduction_age_interval[0]))

    def produce_eatable_offspring(self) -> None:
        min_amount, max_amount = configs.PlantEatableOffspringPossibleAmount.MAPLE_EOPA.value
        for i in range(random.randint(min_amount, max_amount)):
            self._nutritional_value += self._offspring_nutritional_value

    def reproduction(self) -> List:
        min_numb, max_numb = configs.ChanceToProduceKids.MAPLE_CTPK.value
        chance_to_produce = random.randint(min_numb, max_numb)
        if self._can_produce_children() and chance_to_produce == 1:
            min_amount, max_amount = configs.PossibleKidsAmount.MAPLE_PKA.value
            grown_amount = random.randint(min_amount, max_amount)
            return [Maple() for _ in range(grown_amount)]
        return []

    def be_eaten(self, nutritional_value: int) -> int:
        if nutritional_value > self._nutritional_value:
            self._nutritional_value = 0
            self.get_hearted(int(0.5 * (nutritional_value - self._nutritional_value)))
        else:
            self._nutritional_value -= nutritional_value
            self.get_hearted(int(nutritional_value * configs.UnprotectedDamageMultiplier.MAPLE_UDM.value))
        return nutritional_value

    def stats(self) -> str:
        return " Kingdom: Plant" \
               "Kind: Maple" + super().stats()
