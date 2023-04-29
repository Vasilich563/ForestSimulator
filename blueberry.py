#Author Vodohleb04
import configs
from plant import Plant
import configs
from typing import List, NoReturn
import random


class Blueberry(Plant):

    _life_median = configs.LifeMedian.BLUEBERRY_LM.value
    _max_hp = configs.MaxHP.BLUEBERRY_MHP.value
    _offspring_dispersion = configs.PlantOffspringDispersion.BLUEBERRY_OD.value
    _offspring_nutritional_value = configs.NutritionalValue.BLUEBERRY_OFFSPRING_NV.value
    _hp_reduction = configs.PlantHPReduction.BLUEBERRY_HPR.value
    _shrub_reduction = configs.PlantShrubReduction.BLUEBERRY_SR.value
    _start_shrub_nutritional_value = configs.NutritionalValue.START_BLUEBERRY_SNV.value
    _reproduction_age_interval = configs.ReproductionAgeInterval.BLUEBERRY_RAI.value
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
        self._hp = configs.StartHP.BLUEBERRY_START_HP.value
        self._nutritional_value = self._start_shrub_nutritional_value
        super()._make_power_coefficient(configs.PersonalPowerCoefficientParameters.BLUEBERRY_PPCP)
        self._id = configs.IdPrefix.BLUEBERRY_PREF.value + str(self._id_counter)
        Blueberry._id_counter += 1

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        if self.age <= self._life_median:
            return configs.StartPower.BLUEBERRY_SP.value
        else:
            return 3/self.age

    def produce_eatable_offspring(self) -> NoReturn:
        min_amount, max_amount = configs.PlantEatableOffspringPossibleAmount.BLUEBERRY_EOPA.value
        for i in range(random.randint(min_amount, max_amount)):
            self._nutritional_value += self._offspring_nutritional_value

    def reproduction(self) -> List:
        min_numb, max_numb = configs.ChanceToProduceKids.BLUEBERRY_CTPK.value
        chance_to_produce = random.randint(min_numb, max_numb)
        if self._can_produce_children() and chance_to_produce != 0:
            min_amount, max_amount = configs.PossibleKidsAmount.BLUEBERRY_PKA.value
            grown_amount = random.randint(min_amount, max_amount)
            return [Blueberry() for _ in range(grown_amount)]
        return []

    def be_eaten(self, nutritional_value) -> int:
        if nutritional_value > self._nutritional_value:
            self.die()
            return self._nutritional_value
        else:
            self._nutritional_value -= nutritional_value
            self.get_hearted(nutritional_value * configs.UnprotectedDamageMultiplier.BLUEBERRY_UDM.value)
            return nutritional_value

    def stats(self) -> str:
        return """ Kingdom: Plant
 Kind: Blueberry
    """ + super().stats()
