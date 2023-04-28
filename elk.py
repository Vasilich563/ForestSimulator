#Author Vodohleb04
import random
from typing import List, NoReturn
import configs
from animal_types_interfaces import Herbivore
from forest import Hectare


class Elk(Herbivore):

    _life_median = my_enums.LifeMedian.ELK_LM.value
    _reproduction_age_interval = my_enums.ReproductionAgeInterval.ELK_RAI.value
    _id_counter = 0
    _hunger_per_cycle = my_enums.HungerPerCycle.ELK_HPC.value
    _required_nutritional_value = my_enums.RequiredNutritionalValue.ELK_RNV.value

    @staticmethod
    def set_id_counter(new_id_counter) -> NoReturn:
        if new_id_counter < Elk._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >= than old id counter({Elk._id_counter})")
        Elk._id_counter = new_id_counter

    @staticmethod
    def get_id_counter() -> int:
        return Elk._id_counter

    def __init__(self, mother_name=my_enums.CREATOR, father_name=my_enums.CREATOR, unpack_dict_flag=False, info_d=None):
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Elk._id_counter += 1
            return

        self._gender = super()._random_gender()
        if self._gender == my_enums.Genders.MALE:
            ppcp_by_gender = my_enums.PersonalPowerCoefficientParameters.M_ELK_PPCP
        else:
            ppcp_by_gender = my_enums.PersonalPowerCoefficientParameters.FEM_ELK_PPCP
        super()._make_power_coefficient(ppcp_by_gender)
        self._damage = my_enums.Damage.ELK_D.value * self._power_coefficient
        self._age = 0
        self._hp = my_enums.MaxHP.ELK_MHP.value
        self._nutritional_value = my_enums.NutritionalValue.ELK_NV.value
        self._food_energy = self._hunger_per_cycle * 2
        self._id = self._gender.value + "_" + my_enums.IdPrefix.ELK_PREF.value + "_" + str(self._id_counter)
        Elk._id_counter += 1
        self._sterile_period = self._reproduction_age_interval[0]
        self._parents = (mother_name, father_name)

    def _produce_children(self, partner) -> List:
        if partner:
            min_numb, max_numb = my_enums.ChanceToProduceKids.ELK_CTPK.value
            chance_to_produce = random.randint(min_numb, max_numb)
            if chance_to_produce == 1:
                min_amount, max_amount = my_enums.PossibleKidsAmount.ELK_PKA.value
                kids_amount = random.randint(min_amount, max_amount)
                self._sterile_period = my_enums.SterilePeriods.ELK_SP.value
                partner._sterile_period = my_enums.SterilePeriods.ELK_SP.value
                mother_name = self.id if self.gender == my_enums.Genders.FEMALE else partner.id
                father_name = self.id if self.gender == my_enums.Genders.MALE else partner.id
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
        if self._gender == my_enums.Genders.MALE:
            start_power = my_enums.StartPower.M_ELK_SP.value
            k_func_coefficient = my_enums.PowerFunctionCoefficient.M_ELK_PFC.value
        else:
            start_power = my_enums.StartPower.FEM_ELK_SP.value
            k_func_coefficient = my_enums.PowerFunctionCoefficient.FEM_ELK_PFC.value

        if self.age <= self._reproduction_age_interval[0]:  # Progression of power
            return self._power_coefficient * (start_power + (k_func_coefficient * self.age))
        elif self.age <= self._reproduction_age_interval[1]:  # Maximal power (const)
            return self._power_coefficient * (start_power + (k_func_coefficient * self._reproduction_age_interval[0]))
        else:  # Regression of power
            return self._power_coefficient * (start_power + (-k_func_coefficient * self._reproduction_age_interval[0]))

    def stats(self) -> str:
        return """ Kingdom: Animal
    Type: Herbivore
    Kind: Elk
    """ + super().stats()
