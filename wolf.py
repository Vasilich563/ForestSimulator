#Author Vodohleb04
import random
from typing import List, NoReturn
import configs
from animal_types_interfaces import Predator
from forest import Hectare


class Wolf(Predator):

    _life_median = my_enums.LifeMedian.WOLF_LM.value
    _reproduction_age_interval = my_enums.ReproductionAgeInterval.WOLF_RAI.value
    _id_counter = 0
    _hunger_per_cycle = my_enums.HungerPerCycle.WOLF_HPC.value

    @staticmethod
    def set_id_counter(new_id_counter) -> NoReturn:
        if new_id_counter < Wolf._id_counter:
            raise ValueError(f"New id counter({new_id_counter}) must be >= than old id counter({Wolf._id_counter})")
        Wolf._id_counter = new_id_counter

    @staticmethod
    def get_id_counter() -> int:
        return Wolf._id_counter

    def __init__(self, mother_name=my_enums.CREATOR, father_name=my_enums.CREATOR, unpack_dict_flag=False, info_d=None):
        if unpack_dict_flag:
            if not info_d:
                raise ValueError
            super()._unpack_info_from_dict(info_d)
            Wolf._id_counter += 1
            return

        self._gender = super()._random_gender()
        if self._gender == my_enums.Genders.MALE:
            ppcp_by_gender = my_enums.PersonalPowerCoefficientParameters.M_WOLF_PPCP
        else:
            ppcp_by_gender = my_enums.PersonalPowerCoefficientParameters.FEM_WOLF_PPCP
        super()._make_power_coefficient(ppcp_by_gender)
        self._damage = my_enums.Damage.WOLF_D.value * self._power_coefficient
        self._age = 0
        self._hp = my_enums.MaxHP.WOLF_MHP.value
        self._nutritional_value = my_enums.NutritionalValue.WOLF_NV.value
        self._food_energy = self._hunger_per_cycle * 2
        self._id = self._gender.value + "_" + my_enums.IdPrefix.WOLF_PREF.value + "_" + str(self._id_counter)
        Wolf._id_counter += 1
        self._sterile_period = self._reproduction_age_interval[0]
        self._parents = (mother_name, father_name)

    def _produce_children(self, partner) -> List:
        if partner:
            min_numb, max_numb = my_enums.ChanceToProduceKids.WOLF_CTPK.value
            chance_to_produce = random.randint(min_numb, max_numb)
            if chance_to_produce == 1:
                min_amount, max_amount = my_enums.PossibleKidsAmount.WOLF_PKA.value
                kids_amount = random.randint(min_amount, max_amount)
                self._sterile_period = my_enums.SterilePeriods.WOLF_SP.value
                partner._sterile_period = my_enums.SterilePeriods.WOLF_SP.value
                mother_name = self.id if self.gender == my_enums.Genders.FEMALE else partner.id
                father_name = self.id if self.gender == my_enums.Genders.MALE else partner.id
                return [Wolf(mother_name=mother_name, father_name=father_name) for _ in range(kids_amount)]
        return []

    def _can_produce_children(self, partner) -> bool:
        if isinstance(self, Wolf) and isinstance(partner, Wolf):
            return super()._can_produce_children(partner)
        else:
            return False

    def _search_for_partner(self, hectare: Hectare):
        if not isinstance(hectare, Hectare):
            raise TypeError
        for possible_partner in hectare.creations:
            if isinstance(possible_partner, Wolf) and self._can_produce_children(possible_partner):
                return possible_partner
        return None

    def power(self) -> float:
        if self.is_dead():
            return 0.0
        if self._gender == my_enums.Genders.MALE:
            start_power = my_enums.StartPower.M_WOLF_SP.value
            k_func_coefficient = my_enums.PowerFunctionCoefficient.M_WOLF_PFC.value
        else:
            start_power = my_enums.StartPower.FEM_WOLF_SP.value
            k_func_coefficient = my_enums.PowerFunctionCoefficient.FEM_WOLF_PFC.value

        if self.age <= self._reproduction_age_interval[0]:  # Progression of power
            return self._power_coefficient * (start_power + (k_func_coefficient * self.age))
        elif self.age <= self._reproduction_age_interval[1]:  # Maximal power (const)
            return self._power_coefficient * (start_power + (k_func_coefficient * self._reproduction_age_interval[0]))
        else:  # Regression of power
            return self._power_coefficient * (start_power + (-k_func_coefficient * self._reproduction_age_interval[0]))

    def stats(self) -> str:
        return """ Kingdom: Animal
    Type: Predator
    Kind: Wolf
    """ + super().stats()
