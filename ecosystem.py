#Author Vodohleb04
import random
from typing import List, Tuple, Dict

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
        """Returns name of creature from EnglishCreaturesNames

        creature - creature from ecosystem
        raise TypeError if creature\'s type not defined
        """
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
    def _save_creature_to_dict(creature) -> Dict:
        """Makes dict with creature stats (Used to save world to .json file)

        creature - creature from ecosystem
        raise TypeError if creature\'s type not defined
        """
        if not isinstance(creature, Animal) and not isinstance(creature, Plant):
            raise TypeError(f"Not part of ecosystem: {type(creature)}")
        creature_info = creature.get_dict_of_info()
        creature_info["type"] = EcoSystem._define_creature_type(creature)
        return creature_info

    def _fill_forest_with_creatures(self, **kwargs) -> None:
        """Creates creatures and emplace them into forest

        kwargs - dict with amount of creatures of different types
        """
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

    def _unpack_creatures(self, creatures_info_dicts: List[Dict]) -> None:
        """Unpack creatures from dict and emplace them into forest (used in load .json file)

        creatures_info_dict - List of dicts. Dicts contain data about creatures and their stats
        """
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
                self._forest.hectares[i][j].creations.append(Bear(unpack_dict_flag=True, info_dict=creature_info_dict))
            else:
                raise ValueError

    @staticmethod
    def _unpack_id_counters(id_counters_dict) -> None:
        """Rewrites id_counters of creatures type (used in load .json file)

        id_counters_dict - dict with new id_counters of creatures
        """
        Blueberry.rewrite_id_counter(id_counters_dict["blueberry_id_counter"])
        Hazel.rewrite_id_counter(id_counters_dict["hazel_id_counter"])
        Maple.rewrite_id_counter(id_counters_dict["maple_id_counter"])
        Boar.rewrite_id_counter(id_counters_dict["boar_id_counter"])
        Elk.rewrite_id_counter(id_counters_dict["elk_id_counter"])
        Wolf.rewrite_id_counter(id_counters_dict["wolf_id_counter"])
        Bear.rewrite_id_counter(id_counters_dict["bear_id_counter"])

    def __init__(self, filename="", unpack_dict_flag=False, *args, **kwargs):
        """Creates ecosystem
        filename - file to save ecosystem
        unpack_dict_flag - True when need to unpack parameters of ecosystem from dict
        args - creatures stats
        kwargs - params of ecosystem

        EcoSystem - data controller part of program
        """
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
            EcoSystem._unpack_id_counters(args[0])
            self._unpack_creatures(args[1:])
            return
        self._deadly_worm_sleep_counter = self._deadly_worm_sleep_interval
        self._fill_forest_with_creatures(**kwargs)

    def _find_max_id_size(self) -> int:
        """Finds the longest id of creatures at forest"""
        max_id_size = 0
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if max_id_size < len(creature.id):
                        max_id_size = len(creature.id)
        return max_id_size

    def _find_max_amount_in_hectare(self) -> int:
        """Find the maximal amount of creatures in hectare at forest"""
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
        """Defines if ecosystem became wasteland

        True - if there is no creatures in ecosystem
        """
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
        """Provoke movable creatures to change their position"""
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Movable):
                        creature.move(self._forest)

    def _provoke_on_nutrition(self) -> None:
        """Provoke creatures to find food"""
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Hunger):
                        creature.search_for_food(hectare)

    def _provoke_animals_on_reproduction(self) -> None:
        """Provoke animals to make children (find partner to try to make children with)"""
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, GenderReproduction):
                        hectare.extend_hectare(creature.reproduction(hectare))

    def _find_position_in_forest(self, creature: Reproduction) -> Tuple[int, int]:
        """Defines number of hectare where creation is located

        creature - creature in forest, that have id
        returns Tuple(vertical_number_of_hectare, horizontal_number_of_hectare)
        raise ValueError if creature is not exists
        """
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
        """Disperse offsprings in forest on their dispersion distance

        offsprings - list of new NonGenderReproduction creatures
        parent_pos - position of the parent creature(base position to disperse from)
        raise TypeError if creature in offsprings is not NonGenderReproduction creature
        """
        vert_pos, horiz_pos = parent_pos
        for offspring in offsprings:
            if not isinstance(offspring, NonGenderReproduction):
                raise TypeError(f'Offspring must be NonGenderReproduction creature. {type(offspring)} got instead')
            vertical_shift = random.randint(-offspring.offspring_dispersion, offspring.offspring_dispersion)
            horizontal_shift = random.randint(-offspring.offspring_dispersion, offspring.offspring_dispersion)
            while vert_pos + vertical_shift >= self.forest.vertical_length or \
                    horiz_pos + horizontal_shift >= self.forest.horizontal_length:
                vertical_shift = random.randint(-1, 1)
                horizontal_shift = random.randint(-1, 1)
            self.forest.hectares[vert_pos + vertical_shift][horiz_pos + horizontal_shift].creations.append(offspring)

    def _provoke_on_non_gender_reproduction_reproduction(self) -> None:
        """Provokes NonGenderReproduction creatures to make children"""
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, NonGenderReproduction):
                        offsprings = creature.reproduction()
                        parent_position = self._find_position_in_forest(creature)
                        self._disperse_offsprings(offsprings=offsprings, parent_pos=parent_position)

    def _period(self) -> None:
        """Change creatures time-depended parameters and tries to wake deadly_worm"""
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Aging):
                        creature.live_time_cycle()
        self._normal_deadly_worm_period()

    def _normal_deadly_worm_period(self) -> None:
        """Wake deadly worm if it\'s time to wake him

        Deadly worm removes dead creatures from forest
        """
        if self._deadly_worm_sleep_counter == 0:
            self.provoke_deadly_worm()
            self._deadly_worm_sleep_counter = self._deadly_worm_sleep_interval
        else:
            self._deadly_worm_sleep_counter -= 1

    def cycle(self) -> None:
        """Provoke creatures on their time cycle activities"""
        if not self.is_wasteland():
            self._provoke_on_nutrition()
            self._provoke_animals_on_reproduction()
            self._provoke_on_non_gender_reproduction_reproduction()
            self._provoke_on_move()
            self._period()
            # self.sa
            apocalypse_chance = random.randint(1, 100000)
            if apocalypse_chance == 1:
                self.apocalypse()

    def apocalypse(self) -> None:
        """Kills all creatures in forest and wakes deadly_worm on next cycle automatically"""
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Dieable):
                        creature.die()
        self._deadly_worm_sleep_counter = 0

    def provoke_deadly_worm(self) -> None:
        """Removes all dead creatures forcibly (not carries about normal deadly worm periods)"""
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                not_dead_creatures = [creature for creature in hectare.creations if not creature.is_dead()]
                hectare.update_hectare(not_dead_creatures)

    @property
    def forest(self) -> Forest:
        """Returns data container forest"""
        return self._forest

    def remove_creature(self, creature_id: str) -> None:
        """Removes creature from ecosystem

        creature_id - id of creature to remove
        raise ValueError if creature is not exists
        """
        for hectare_line in self.forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if isinstance(creature, Reproduction) and creature_id == creature.id:
                        hectare.creations.remove(creature)
                        return
        raise ValueError(f"No creature with id {creature_id}")

    def fill_creatures(self, creature_type: str, creature_amount: int, hectare_number: Tuple[int, int]) -> None:
        """Adds creatures to ecosystem

        creature_type - type of creature to add
        creature_amount - amount_of_creature to add
        hectare_number: Tuple(vertical_number: int, horizontal_number: int) - number of hectare to add creatures
            vertical_number - vertical number of hectare to add creatures
            horizontal_number - horizontal number of hectare to add creatures

        raise Index error if number of hectare is out of length of forest
        raise TypeError if creature_type is not defined in ecosystem (unknown type of creature)
        """
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
        """Returns save filename"""
        return self._filename

    @filename.setter
    def filename(self, new_filename: str) -> None:
        """Sets new filename

        new_filename - new file to save ecosystem
        raise ValueError if type of file is not .json
        """
        if not new_filename.endswith(".json"):
            raise ValueError(f"Unknown type of file: {new_filename} (expected \".json\")")
        self._filename = new_filename

    def load(self, filename):
        """Loads ecosystem from file

        filename - .json file to load ecosystem from
        raise ValueError if type of file is not .json
        """
        if not filename.endswith(".json"):
            raise ValueError(f"Unknown type of file: {filename} (expected \".json\")")
        with open(filename, "r") as save_file:
            loaded_info = json.load(save_file)
            ecosystem_info = loaded_info[0]
            unpack_dict_flag = True
            self.__init__(filename, unpack_dict_flag, *loaded_info[1:], **ecosystem_info)

    def _pack_general_data(self) -> List:
        """Emplace params of ecosystem to dict (used to save ecosystem)"""
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
        """Defines name for save file"""
        import os
        import re
        regex = re.compile(configs.FileRegex.AUTOSAVE_REGEX.value)
        filename_indexes = [int(regex.match(file).group(1)) for file in os.listdir(configs.BASIC_SAVES_DIR_LINUX_PATH) if regex.match(file)]
        if not filename_indexes:
            filename_indexes.append(0)
        return f"{configs.BASIC_SAVES_DIR_LINUX_PATH}autosave{max(filename_indexes) + 1}.json"

    def save(self, filename="") -> None:
        """Saves ecosystem

        filename - .json file to save ecosystem
        raise ValueError if filename is not .json file
        """
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
        """Finds creature in forest

        creature_id - id of creature to find
        returns Creature with id == creature_id
        returns None if creature is not found
        """
        if creature_id == configs.GuiMessages.WASTELAND_CREATURES_INFO.value:
            return configs.GuiMessages.WASTELAND_CREATURES_INFO
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if (isinstance(creature, Animal) or isinstance(creature, Plant)) and creature_id == creature.id:
                        return creature
        return None

    def console_creature_stats(self, creature_id) -> str:
        """Returns str with stats of creature

        creature_id - id of creature to show stats
        raise ValueError if creature is not exists

        used in console mode
        """
        for hectare_line in self._forest.hectares:
            for hectare in hectare_line:
                for creature in hectare.creations:
                    if (isinstance(creature, Animal) or isinstance(creature, Plant)) and creature_id == creature.id:
                        return creature.stats()
        raise ValueError(f"No creature with id {creature_id}")

    def get_creature_icon_file(self, creature) -> str:
        """Returns file with icon for creature stats dialog

        creature - creature to show stats

        used in graphic mode
        """
        if creature.is_dead():
            return configs.CREATURES_ICONS["grave_icon"]
        return configs.CREATURES_ICONS[f"{self._define_creature_type(creature)}_icon"]

    @staticmethod
    def define_reproduction_type(creature) -> configs.ReproductionType:
        """Defines type of reproduction of creature

        creature_id - id of creature to show stats
        raise ValueError if creature has unexpected type
        """
        if isinstance(creature, NonGenderReproduction):
            return configs.ReproductionType.NON_GENDER_REPRODUCTION
        elif isinstance(creature, GenderReproduction):
            return configs.ReproductionType.GENDER_REPRODUCTION
        else:
            raise ValueError(f"unknown creature, type: {type(creature)}")

    @staticmethod
    def define_creature_kind_from_russian(creature_russian_name: str) -> str:
        """Returns english name of creature type

        creature_russian_name - russian name of creature type
        raise ValueError if creature has unexpected type
        """
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
    def define_creature_kind(creature) -> str:
        """Returns english name of creature

        creature - creature to define kind
        """
        return EcoSystem._define_creature_type(creature)

    @staticmethod
    def define_creature_kingdom(creature) -> configs.CreatureType:
        """Returns name of creature kingdom

        creature - creature to define kingdom
        raise ValueError if creature has unexpected type
        """
        if isinstance(creature, Animal):
            return configs.CreatureType.ANIMAL
        elif isinstance(creature, Plant):
            return configs.CreatureType.PLANT
        else:
            raise ValueError(f"Неизвестный тип существ: {type(creature)}")

    @staticmethod
    def define_creature_nutrition_type(creature) -> configs.NutritionType:
        """Defines type of nutrition of creature

        creature - creature to define type of nutrition
        raise ValueError if creature has unexpected type
        """
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

    def count_creatures_amount(self) -> int:
        """Counts amount of creatures in forest

        raise TypeError if creature\'s type not defined
        """
        creatures_counter = 0
        for i in range(self._forest.vertical_length):
            for j in range(self._forest.horizontal_length):
                for k in range(len(self._forest.hectares[i][j].creations)):
                    self._define_creature_type(self._forest.hectares[i][j].creations[k])
                    creatures_counter += 1
        return creatures_counter


