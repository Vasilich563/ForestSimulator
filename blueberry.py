#Author Vodohleb04
import configs
from plant import Plant
import configs
from typing import List, NoReturn
import random


class Blueberry(Plant):

    _life_median = my_enums.LifeMedian.BLUEBERRY_LM.value
    _max_hp = my_enums.MaxHP.BLUEBERRY_MHP.value
    _offspring_dispersion = my_enums.PlantOffspringDispersion.BLUEBERRY_OD.value
    _offspring_nutritional_value = my_enums.NutritionalValue.BLUEBERRY_OFFSPRING_NV.value
    _hp_reduction = my_enums.PlantHPReduction.BLUEBERRY_HPR.value
    _shrub_reduction = my_enums.PlantShrubReduction.BLUEBERRY_SR.value
    _start_shrub_nutritional_value = my_enums.NutritionalValue.START_BLUEBERRY_SNV.value
    _reproduction_age_interval = my_enums.ReproductionAgeInterval.BLUEBERRY_RAI.value
    _id_counter = 0

    @staticmethod
    def set_id_counter(new_id_counter) -> NoReturn:
        if new_id_counter < Blueberry._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >="
                             f" than old id counter({Blueberry._id_counter})")
        Blueberry._id_counter = new_id_counter

    @staticmethod
    def get_id_counter() -> int:
        return Blueberry._id_counter

    def __init__(self, unpack_dict_flag=False, info_d=None):
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Blueberry._id_counter += 1
            return

        self._age = 0
        self._hp = my_enums.StartHP.BLUEBERRY_START_HP.value
        self._nutritional_value = self._start_shrub_nutritional_value
        super()._make_power_coefficient(my_enums.PersonalPowerCoefficientParameters.BLUEBERRY_PPCP)
        self._id = my_enums.IdPrefix.BLUEBERRY_PREF.value + str(self._id_counter)
        Blueberry._id_counter += 1

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        if self.age <= self._life_median:
            return my_enums.StartPower.BLUEBERRY_SP.value
        else:
            return 3/self.age

    def produce_eatable_offspring(self) -> NoReturn:
        min_amount, max_amount = my_enums.PlantEatableOffspringPossibleAmount.BLUEBERRY_EOPA.value
        for i in range(random.randint(min_amount, max_amount)):
            self._nutritional_value += self._offspring_nutritional_value

    def reproduction(self) -> List:
        min_numb, max_numb = my_enums.ChanceToProduceKids.BLUEBERRY_CTPK.value
        chance_to_produce = random.randint(min_numb, max_numb)
        if self._can_produce_children() and chance_to_produce != 0:
            min_amount, max_amount = my_enums.PossibleKidsAmount.BLUEBERRY_PKA.value
            grown_amount = random.randint(min_amount, max_amount)
            return [Blueberry() for _ in range(grown_amount)]
        return []

    def be_eaten(self, nutritional_value) -> int:
        if nutritional_value > self._nutritional_value:
            self.die()
            return self._nutritional_value
        else:
            self._nutritional_value -= nutritional_value
            self.get_hearted(nutritional_value * my_enums.UnprotectedDamageMultiplier.BLUEBERRY_UDM.value)
            return nutritional_value

    def stats(self) -> str:
        return """ Kingdom: Plant
 Kind: Blueberry
    """ + super().stats()
