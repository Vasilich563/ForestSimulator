#Author Vodohleb04
import random
from typing import List, Tuple

import animal_types_interfaces
import configs
from forest import Forest
from blueberry import Blueberry
from hazel import Hazel
from maple import Maple
from boar import Boar
from elk import Elk
from wolf import Wolf
from bear import Bear
from creature_interfaces import Movable, Hunger, Aging, Dieable
from reproduction import GenderReproduction, NonGenderReproduction, Reproduction
from plant import Plant
from animal import Animal
import json


class EcoSystem:

    @staticmethod
    def _define_creature_type(creature) -> str:
        if isinstance(creature, Blueberry):
            return configs.EnglishCreaturesNames.BLUEBERRY.value
        elif isinstance(creature, Hazel):
            return configs.EnglishCreaturesNames.HAZEL.value
        elif isinstance(creature, Maple):
            return configs.EnglishCreaturesNames.MAPLE.value
        elif isinstance(creature, Boar):
            return configs.EnglishCreaturesNames.BOAR.value
        elif isinstance(creature, Elk):
            return configs.EnglishCreaturesNames.ELK.value
        elif isinstance(creature, Wolf):
            return configs.EnglishCreaturesNames.WOLF.value
        elif isinstance(creature, Bear):
            return configs.EnglishCreaturesNames.BEAR.value
        else:
            raise TypeError(f"Not part of ecosystem: {type(creature)}")

    @staticmethod
    def _save_creature_to_dict(creature) -> dict:
        if not isinstance(creature, Animal) and not isinstance(creature, Plant):
            raise TypeError(f"Not part of ecosystem: {type(creature)}")
        creature_info = creature.get_dict_of_info()
        creature_info["type"] = EcoSystem._define_creature_type(creature)
        return creature_info

    def _fill_forest_with_creatures(self, **kwargs) -> None:
        kwargs[f"{configs.EnglishCreaturesNames.BLUEBERRY.value}_amount"] = kwargs.get(
            f"{configs.EnglishCreaturesNames.BLUEBERRY.value}_amount", 20)
        kwargs[f"{configs.EnglishCreaturesNames.HAZEL.value}_amount"] = kwargs.get(
            f"{configs.EnglishCreaturesNames.HAZEL.value}_amount", 10)
        kwargs[f"{configs.EnglishCreaturesNames.MAPLE.value}_amount"] = kwargs.get(
            f"{configs.EnglishCreaturesNames.MAPLE.value}_amount", 10)
        kwargs[f"{configs.EnglishCreaturesNames.BOAR.value}_amount"] = kwargs.get(
            f"{configs.EnglishCreaturesNames.BOAR.value}_amount", 12)
        kwargs[f"{configs.EnglishCreaturesNames.ELK.value}_amount"] = kwargs.get(
            f"{configs.EnglishCreaturesNames.ELK.value}_amount", 6)
        kwargs[f"{configs.EnglishCreaturesNames.WOLF.value}_amount"] = kwargs.get(
            f"{configs.EnglishCreaturesNames.WOLF.value}_amount", 12)
        kwargs[f"{configs.EnglishCreaturesNames.BEAR.value}_amount"] = kwargs.get(
            f"{configs.EnglishCreaturesNames.BEAR.value}_amount", 6)
        for key, value in kwargs.items():
            if key.endswith("_amount"):
                new_key = key.replace("_amount", "")
                for _ in range(value):
                    random_line_number = random.randint(0, self.forest.vertical_length - 1)
                    random_column_number = random.randint(0, self.forest.horizontal_length - 1)
                    self.fill_creatures(new_key, 1, (random_line_number, random_column_number))

    def _unpack_creatures(self, creatures_info_dicts: List) -> None:
        for creature_info_dict in creatures_info_dicts:
            i, j = creature_info_dict["position"]
            if creature_info_dict["type"] == configs.EnglishCreaturesNames.BLUEBERRY.value:
                self._forest.hectares[i][j].creations.append(Blueberry(unpack_dict_flag=True,
                                                                       info_d=creature_info_dict))
            elif creature_info_dict["type"] == configs.EnglishCreaturesNames.HAZEL.value:
                self._forest.hectares[i][j].creations.append(Hazel(unpack_dict_flag=True, info_d=creature_info_dict))
            elif creature_info_dict["type"] == configs.EnglishCreaturesNames.MAPLE.value:
                self._forest.hectares[i][j].creations.append(Maple(unpack_dict_flag=True, info_d=creature_info_dict))
            elif creature_info_dict["type"] == configs.EnglishCreaturesNames.BOAR.value:
                self._forest.hectares[i][j].creations.append(Boar(unpack_dict_flag=True, info_d=creature_info_dict))
            elif creature_info_dict["type"] == configs.EnglishCreaturesNames.ELK.value:
                self._forest.hectares[i][j].creations.append(Elk(unpack_dict_flag=True, info_d=creature_info_dict))
            elif creature_info_dict["type"] == configs.EnglishCreaturesNames.WOLF.value:
                self._forest.hectares[i][j].creations.append(Wolf(unpack_dict_flag=True, info_d=creature_info_dict))
            elif creature_info_dict["type"] == configs.EnglishCreaturesNames.BEAR.value:
                self._forest.hectares[i][j].creations.append(Bear(unpack_dict_flag=True, info_d=creature_info_dict))
            else:
                raise ValueError

    @staticmethod
    def _unpack_id_counters(id_counters_dict) -> None:
        Blueberry.rewrite_id_counter(id_counters_dict["blueberry_id_counter"])
        Hazel.rewrite_id_counter(id_counters_dict["hazel_id_counter"])
        Maple.rewrite_id_counter(id_counters_dict["maple_id_counter"])
        Boar.rewrite_id_counter(id_counters_dict["boar_id_counter"])
        Elk.rewrite_id_counter(id_counters_dict["elk_id_counter"])
        Wolf.rewrite_id_counter(id_counters_dict["wolf_id_counter"])
        Bear.rewrite_id_counter(id_counters_dict["bear_id_counter"])

    def __init__(self, filename="", unpack_dict_flag=False, *args, **kwargs):
        if filename and not filename.endswith(".json"):
            raise ValueError(f"Unknown type of file: {filename} (expected.json)")
        self._filename = filename
        kwargs["forest_vertical_length"] = kwargs.get("forest_vertical_length", 4)
        kwargs["forest_horizontal_length"] = kwargs.get("forest_horizontal_length", 4)
        kwargs["deadly_worm_sleep_interval"] = kwargs.get("deadly_worm_sleep_interval", 5)
        if unpack_dict_flag:
            kwargs["deadly_worm_sleep_counter"] = kwargs.get("deadly_worm_sleep_counter", 5)
        self._forest = Forest(vertical_length=kwargs["forest_vertical_length"],
                              horizontal_length=kwargs["forest_horizontal_length"])
        self._deadly_worm_sleep_interval = kwargs["deadly_worm_sleep_interval"]
        if unpack_dict_flag:
            self._deadly_worm_sleep_counter = kwargs["deadly_worm_sleep_counter"]
            print(args[0])
            EcoSystem._unpack_id_counters(args[0])
            self._unpack_creatures(args[1:])
            return

        self._deadly_worm_sleep_counter = self._deadly_worm_sleep_interval
        self._fill_forest_with_creatures(**kwargs)

    def _find_max_id_size(self) -> int:
        max_id_size = 0
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if max_id_size < len(creature.id):
                        max_id_size = len(creature.id)
        return max_id_size

    def _find_max_amount_in_hectare(self) -> int:
        max_amount = 0
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                if len(hectare.creations) > max_amount:
                    max_amount = len(hectare.creations)
        return max_amount

    def __str__(self):
        from math import log10
        if self.is_wasteland():
            return self._show_wasteland()
        max_id = self._find_max_id_size()
        max_amount_in_hectare = self._find_max_amount_in_hectare()
        res_str = f"{'':<{int(log10(self.forest.vertical_length) + 1)}}|"
        for i in range(self.forest.horizontal_length):
            res_str += f"{i:<{max_id}}|"
        res_str += "\n"

        for i in range(self.forest.vertical_length):
            res_str += ("-" * int(log10(self.forest.vertical_length) + 1)) + "+"
            for _ in range(self.forest.horizontal_length):
                res_str += ("-" * max_id) + "+"
            res_str += "\n"

            print_number = True
            for k in range(max_amount_in_hectare):
                vertical_number_of_hectare = str(i) if print_number else ""
                print_number = False
                res_str += f"{vertical_number_of_hectare:<{int(log10(self.forest.vertical_length) + 1)}}|"
                for j in range(self._forest.horizontal_length):
                    try:
                        res_str += f"{str(self.forest.hectares[i][j].creations[k]):<{max_id}}|"
                    except IndexError:
                        res_str += f"{'':<{max_id}}|"
                res_str += f"\n"
        return res_str

    def is_wasteland(self) -> bool:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Plant) or isinstance(creature, Animal):
                        return False
        return True

    def _show_wasteland(self) -> str:
        from math import log10
        max_id = len("great_wasteland")
        res_str = f"{'':<{int(log10(self.forest.vertical_length) + 1)}}|"
        for i in range(self.forest.horizontal_length):
            res_str += f"{i:<{max_id}}|"
        res_str += "\n"
        for i in range(self.forest.vertical_length):
            res_str += ("-" * int(log10(self.forest.vertical_length) + 1)) + "+"
            for _ in range(self.forest.horizontal_length):
                res_str += ("-" * max_id) + "+"
            res_str += "\n"
            res_str += f"{i:<{int(log10(self.forest.vertical_length) + 1)}}|"
            for _ in range(self.forest.horizontal_length):
                res_str += "great_wasteland|"
            res_str += "\n"
        return res_str

    def _provoke_on_move(self) -> None:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Movable):
                        creature.move(self._forest)

    def _provoke_on_nutrition(self) -> None:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Hunger):
                        creature.search_for_food(hectare)

    def _provoke_animals_on_reproduction(self) -> None:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, GenderReproduction):
                        hectare.extend_hectare(creature.reproduction(hectare))

    def _find_position_in_forest(self, creature: Reproduction) -> Tuple[int, int]:
        not_found_flag = True
        i = 0
        j = 0
        for hectare_line in self.forest.hectares:
            j = 0
            for hectare in hectare_line:
                if creature in hectare.creations:
                    not_found_flag = False
                    break
                j += 1
            else:
                i += 1
                continue
            break
        if not_found_flag:
            raise ValueError(f"Creature with id {creature.id} wasn't found in forest")
        return i, j

    def _disperse_offsprings(self, offsprings: List[NonGenderReproduction], parent_pos: Tuple[int, int]) -> None:
        vert_pos, horiz_pos = parent_pos
        for offspring in offsprings:
            if not isinstance(offspring, Plant):
                raise TypeError(f'Offspring must be Plant. {type(offspring)} got instead')
            vertical_shift = random.randint(-offspring.offspring_dispersion, offspring.offspring_dispersion)
            horizontal_shift = random.randint(-offspring.offspring_dispersion, offspring.offspring_dispersion)
            while vert_pos + vertical_shift >= self.forest.vertical_length or \
                    horiz_pos + horizontal_shift >= self.forest.horizontal_length:
                vertical_shift = random.randint(-1, 1)
                horizontal_shift = random.randint(-1, 1)
            self.forest.hectares[vert_pos + vertical_shift][horiz_pos + horizontal_shift].creations.append(offspring)

    def _provoke_plants_on_reproduction(self) -> None:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, NonGenderReproduction):
                        offsprings = creature.reproduction()
                        parent_position = self._find_position_in_forest(creature)
                        self._disperse_offsprings(offsprings=offsprings, parent_pos=parent_position)

    def _period(self) -> None:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Aging):
                        creature.live_time_cycle()
        self._normal_deadly_worm_period()

    def _normal_deadly_worm_period(self) -> None:
        if self._deadly_worm_sleep_counter == 0:
            self.provoke_deadly_worm()
            self._deadly_worm_sleep_counter = self._deadly_worm_sleep_interval
        else:
            self._deadly_worm_sleep_counter -= 1

    def cycle(self) -> None:
        if not self.is_wasteland():
            self._provoke_on_nutrition()
            self._provoke_animals_on_reproduction()
            self._provoke_plants_on_reproduction()
            self._provoke_on_move()
            self._period()
            # self.sa
            apocalypse_chance = random.randint(1, 100000)
            if apocalypse_chance == 1:
                self.apocalypse()

    def apocalypse(self) -> None:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Dieable):
                        creature.die()
        self._deadly_worm_sleep_counter = 0

    def provoke_deadly_worm(self) -> None:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                not_dead_creatures = [creature for creature in hectare.creations if not creature.is_dead()]
                hectare.update_hectare(not_dead_creatures)

    @property
    def forest(self) -> Forest:
        return self._forest

    def remove_creature(self, creature_id: str) -> None:
        for hectare_line in self.forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Reproduction) and creature_id == creature.id:
                        hectare.creations.remove(creature)
                        return
        raise ValueError(f"No creature with id {creature_id}")

    def fill_creatures(self, creature_type: str, creature_amount: int, hectare_number: Tuple[int, int]) -> None:
        if not 0 <= hectare_number[0] < self.forest.vertical_length or\
                not 0 <= hectare_number[1] < self.forest.horizontal_length:
            raise IndexError("Hectare out of forest")
        creature_type = creature_type.lower()
        if creature_type == configs.EnglishCreaturesNames.BLUEBERRY.value:
            creatures = [Blueberry() for _ in range(creature_amount)]
        elif creature_type == configs.EnglishCreaturesNames.HAZEL.value:
            creatures = [Hazel() for _ in range(creature_amount)]
        elif creature_type == configs.EnglishCreaturesNames.MAPLE.value:
            creatures = [Maple() for _ in range(creature_amount)]
        elif creature_type == configs.EnglishCreaturesNames.BOAR.value:
            creatures = [Boar() for _ in range(creature_amount)]
        elif creature_type == configs.EnglishCreaturesNames.ELK.value:
            creatures = [Elk() for _ in range(creature_amount)]
        elif creature_type == configs.EnglishCreaturesNames.WOLF.value:
            creatures = [Wolf() for _ in range(creature_amount)]
        elif creature_type == configs.EnglishCreaturesNames.BEAR.value:
            creatures = [Bear() for _ in range(creature_amount)]
        else:
            raise TypeError(f"Incorrect type of creature: {creature_type}")
        self.forest.hectares[hectare_number[0]][hectare_number[1]].extend_hectare(creatures)

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, new_filename: str) -> None:
        if not new_filename.endswith(".json"):
            raise ValueError(f"Unknown type of file: {new_filename} (expected \".json\")")
        self._filename = new_filename

    def load(self, filename):
        if not filename.endswith(".json"):
            raise ValueError(f"Unknown type of file: {filename} (expected \".json\")")
        with open(filename, "r") as save_file:
            loaded_info = json.load(save_file)
            ecosystem_info = loaded_info[0]
            unpack_dict_flag = True
            self.__init__(filename, unpack_dict_flag, *loaded_info[1:], **ecosystem_info)

    def _pack_general_data(self) -> List:
        return [
            {
                "deadly_worm_sleep_interval": self._deadly_worm_sleep_interval,
                "deadly_worm_sleep_counter": self._deadly_worm_sleep_counter,
                "forest_horizontal_length": self._forest.horizontal_length,
                "forest_vertical_length": self._forest.vertical_length
            },
            {
                "blueberry_id_counter": Blueberry.get_id_counter(),
                "hazel_id_counter": Hazel.get_id_counter(),
                "maple_id_counter": Maple.get_id_counter(),
                "boar_id_counter": Boar.get_id_counter(),
                "elk_id_counter": Elk.get_id_counter(),
                "wolf_id_counter": Wolf.get_id_counter(),
                "bear_id_counter": Bear.get_id_counter()
            }
        ]

    def _define_autosave_file(self) -> str:
        import os
        import re
        regex = re.compile(configs.FileRegex.AUTOSAVE_REGEX.value)
        filename_indexes = [int(regex.match(file).group(1)) for file in os.listdir(configs.BASIC_SAVES_DIR_LINUX_PATH) if regex.match(file)]
        if not filename_indexes:
            filename_indexes.append(0)
        return f"{configs.BASIC_SAVES_DIR_LINUX_PATH}autosave{max(filename_indexes) + 1}.json"



    def save(self, filename="") -> None:
        if not filename:
            filename = self._filename if self._filename else self._define_autosave_file()
        if not filename.endswith(".json"):
            raise ValueError(f"Unknown type of file: {filename} (expected \".json\")")
        res_lst = self._pack_general_data()
        i = 0
        for hectare_line in self.forest.hectares:
            j = 0
            for hectare in hectare_line:
                if hectare.creations:
                    for creature in hectare.creations:
                        if isinstance(creature, Animal) or isinstance(creature, Plant):
                            creature_info = EcoSystem._save_creature_to_dict(creature)
                            creature_info["position"] = (i, j)
                            res_lst.append(creature_info)
                j += 1
            i += 1
        with open(filename, "w") as save_file:
            json.dump(res_lst, save_file, indent="\t")

    def find_creature(self, creature_id):
        if creature_id == configs.GuiMessages.WASTELAND_CREATURES_INFO.value:
            return configs.GuiMessages.WASTELAND_CREATURES_INFO
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if (isinstance(creature, Animal) or isinstance(creature, Plant)) and creature_id == creature.id:
                        return creature

    def console_creature_stats(self, creature_id) -> str:
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if (isinstance(creature, Animal) or isinstance(creature, Plant)) and creature_id == creature.id:
                        return creature.stats()
        raise ValueError(f"No creature with id {creature_id}")

    def get_creature_icon_file(self, creature):
        if creature.is_dead():
            return configs.CREATURES_ICONS["grave_icon"]
        return configs.CREATURES_ICONS[f"{self._define_creature_type(creature)}_icon"]

    @staticmethod
    def define_reproduction_type(creature) -> configs.ReproductionType:
        if isinstance(creature, NonGenderReproduction):
            return configs.ReproductionType.NON_GENDER_REPRODUCTION
        elif isinstance(creature, GenderReproduction):
            return configs.ReproductionType.GENDER_REPRODUCTION
        else:
            raise ValueError(f"unknown creature, type: {type(creature)}")

    @staticmethod
    def define_creature_kind_from_russian(creature_russian_name: str):
        if creature_russian_name == configs.RussianCreaturesNames.BLUEBERRY.value:
            return configs.EnglishCreaturesNames.BLUEBERRY.value
        elif creature_russian_name == configs.RussianCreaturesNames.HAZEL.value:
            return configs.EnglishCreaturesNames.HAZEL.value
        elif creature_russian_name == configs.RussianCreaturesNames.MAPLE.value:
            return configs.EnglishCreaturesNames.MAPLE.value
        elif creature_russian_name == configs.RussianCreaturesNames.BOAR.value:
            return configs.EnglishCreaturesNames.BOAR.value
        elif creature_russian_name == configs.RussianCreaturesNames.ELK.value:
            return configs.EnglishCreaturesNames.ELK.value
        elif creature_russian_name == configs.RussianCreaturesNames.WOLF.value:
            return configs.EnglishCreaturesNames.WOLF.value
        elif creature_russian_name == configs.RussianCreaturesNames.BEAR.value:
            return configs.EnglishCreaturesNames.BEAR.value
        else:
            ValueError(f"Unknown type of creature: {creature_russian_name}")

    @staticmethod
    def define_creature_kind(creature):
        return EcoSystem._define_creature_type(creature)

    @staticmethod
    def define_creature_kingdom(creature) -> configs.CreatureType:
        if isinstance(creature, Animal):
            return configs.CreatureType.ANIMAL
        elif isinstance(creature, Plant):
            return configs.CreatureType.PLANT
        else:
            raise ValueError(f"Неизвестный тип существ: {type(creature)}")

    @staticmethod
    def define_creature_nutrition_type(creature) -> configs.NutritionType:
        if isinstance(creature, Plant):
            return configs.NutritionType.AUTOTROPH
        elif isinstance(creature, animal_types_interfaces.Herbivore):
            return configs.NutritionType.HERBIVORE
        elif isinstance(creature, animal_types_interfaces.Predator):
            return configs.NutritionType.PREDATOR
        elif isinstance(creature, animal_types_interfaces.Omnivorous):
            return configs.NutritionType.OMNIVOROUS
        else:
            raise ValueError(f"Неизвестный тип существ: {type(creature)}")



