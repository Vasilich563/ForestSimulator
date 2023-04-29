#Author Vodohleb04
import enum
import os

import configs
from ecosystem import EcoSystem
from typing import NoReturn


class ExitCodes(enum.Enum):
    NORMAL_END_SAVED = 0
    NORMAL_END_NOT_SAVED = 1
    WARNING_END_LOST_SAVED = 2
    REMOVABLE_INPUT_ERROR = 3
    ERROR_UNKNOWN_TYPE_OF_PARAMETER = -1
    ERROR_INCORRECT_VALUE = -2


class GameEndedException(Exception):

    def __init__(self, exit_code: ExitCodes, filename=""):
        if exit_code == ExitCodes.ERROR_INCORRECT_VALUE or exit_code == ExitCodes.ERROR_UNKNOWN_TYPE_OF_PARAMETER:
            msg = "Simulation stopped by error!"
        elif exit_code == ExitCodes.REMOVABLE_INPUT_ERROR:
            msg = "New input is required"
        elif exit_code == ExitCodes.NORMAL_END_NOT_SAVED:
            msg = "Game is ended without save."
        else:
            if filename:
                msg = f"Game is ended and saved to file \"{filename}\"."
            else:
                exit_code = ExitCodes.WARNING_END_LOST_SAVED
                msg = "Game is ended. Name of file is lost. It may cause a disappearance of save."
        self._exit_code = exit_code
        self._msg = msg
        super().__init__(msg)

    @property
    def message(self) -> str:
        return self._msg

    @property
    def exit_code(self) -> ExitCodes:
        return self._exit_code




def input_ecosystem_parameter(parameter_name: str, can_be_zero=False) -> int:
    parameter = -1
    while parameter < 0 - can_be_zero:
        try:
            parameter = int(input(f"Input {parameter_name}:\t"))
        except ValueError:
            parameter = -1
    return parameter


def help_command() -> NoReturn:
    print(HELP_MESSAGE)


def start_command(ecosystem, ecosystem_exists_flag) -> EcoSystem:
    if ecosystem_exists_flag:
        try:
            exit_command(ecosystem, ecosystem_exists_flag)
        except GameEndedException as ex:
            os.system("clear")
            print(ex.message)
            input("Press Enter to continue")
    automatic_fill = input("Do you want to input parameters by yourself? yes(y) / no (n). Input \"help\""
                           "to get clarification.\t").lower()
    while automatic_fill != "yes" and automatic_fill != "y" and automatic_fill != "no" and automatic_fill != "n":
        if automatic_fill == "help":
            print(HELP_MESSAGE)
        automatic_fill = input("Do you want to input parameters by yourself? yes(y) / no (n) Input \"help\""
                               "to get clarification.\t").lower()
    if automatic_fill == "yes" or automatic_fill == "y":
        ecosystem_parameters = {
            "forest_vertical_length": input_ecosystem_parameter("vertical length of forest"),
            "forest_horizontal_length": input_ecosystem_parameter("horizontal length of forest"),
            "deadly_worm_sleep_interval": input_ecosystem_parameter("sleep interval of deadly worm", can_be_zero=True),
            "blueberry_amount": input_ecosystem_parameter("amount of blueberries", can_be_zero=True),
            "haze_amount": input_ecosystem_parameter("amount of hazels", can_be_zero=True),
            "maple_amount": input_ecosystem_parameter("amount of maples", can_be_zero=True),
            "boar_amount": input_ecosystem_parameter("amount of boars", can_be_zero=True),
            "elk_amount": input_ecosystem_parameter("amount of elks", can_be_zero=True),
            "wolf_amount": input_ecosystem_parameter("amount of wolfs", can_be_zero=True),
            "bear_amount": input_ecosystem_parameter("amount of bears", can_be_zero=True)
        }
    else:
        ecosystem_parameters = configs.BASE_ECOSYSTEM_PARAMETERS
    return EcoSystem(**ecosystem_parameters)


def exit_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    choice = input("Are you sure you want to exit? yes(y) / no (n) Input \"help\""
                   "to get clarification.\t").lower()
    while choice != "yes" and choice != "y" and choice != "no" and choice != "n":
        if choice == "help":
            print(HELP_MESSAGE)
        choice = input("Are you sure you want to exit? yes(y) / no (n) Input \"help\""
                       "to get clarification.\t").lower()
    if choice == "no" or choice == "n":
        return
    else:
        choice = input("Are you want to save the game before exit? yes(y) / no (n) Input \"help\""
                       "to get clarification.\t").lower()
        while choice != "yes" and choice != "y" and choice != "no" and choice != "n":
            if choice == "help":
                print(HELP_MESSAGE)
            choice = input("Are you want to save the game before exit? yes(y) / no (n) Input \"help\""
                           "to get clarification.\t").lower()
        if choice == "yes" or choice == "y":
            filename = save_command(ecosystem, ecosystem_exists_flag)
            raise GameEndedException(filename=filename, exit_code=ExitCodes.NORMAL_END_SAVED)
        else:
            raise GameEndedException(exit_code=ExitCodes.NORMAL_END_NOT_SAVED)


def save_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> str:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    filename = input("Input the name of .json file to save your game):\t")
    if not filename.endswith(".json"):
        raise ValueError(f"{filename} is not .json file")
    ecosystem.save(filename)
    return filename


def load_command(ecosystem, ecosystem_exists_flag) -> EcoSystem:
    if ecosystem_exists_flag:
        try:
            exit_command(ecosystem, ecosystem_exists_flag)
        except GameEndedException as ex:
            os.system("clear")
            print(ex.message)
            input("Press Enter to continue")
    filename = input("Input the name of .json file with saved game to load your game):\t")
    if not filename.endswith(".json"):
        raise ValueError(f"{filename} is not .json file")
    return EcoSystem.load(filename)


def period_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    ecosystem.cycle()
    os.system("clear")
    print(ecosystem)


def add_creature_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    print("""Commands to create creature:
 --blueberry or -bb
 --hazel or -h
 --maple or -m
 --boar or -bo
 --elk or -e
 --wolf or -w
 --bear or -be""")
    creature_type_command = input("Input creature type: Input \"help\" to get clarification.\t")
    if creature_type_command.lower() == "help":
        print(HELP_MESSAGE)
        creature_type_command = input("Input creature type:\t")
    define_creature_type(ecosystem, creature_type_command, ecosystem_exists_flag)


def creature_stats_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    creature_id = input("Input id of creature to show its stats")
    lower_creature_id = creature_id.lower()
    print(ecosystem.creature_stats(lower_creature_id))


def define_creature_type(ecosystem: EcoSystem, creature_type_command: str, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    str_with_hectare_number = input("Input hectare number in form: \'vertical number\', 'horizontal number'):\t")
    hectare_number = [int(p) for p in str_with_hectare_number.replace(" ", "").split(",")]
    if not len(hectare_number) == 2:
        raise ValueError(f"Incorrect input {str_with_hectare_number}")
    lower_creature_type_command = creature_type_command.lower()
    wrong_command = True
    while wrong_command:
        wrong_command = False
        if lower_creature_type_command == "--blueberry" or lower_creature_type_command == "-bb":
            ecosystem.fill_creatures("blueberry", creature_amount=1, hectare_number=tuple(hectare_number))
        elif lower_creature_type_command == "--hazel" or lower_creature_type_command == "-h":
            ecosystem.fill_creatures("hazel", creature_amount=1, hectare_number=tuple(hectare_number))
        elif lower_creature_type_command == "--maple" or lower_creature_type_command == "-m":
            ecosystem.fill_creatures("maple", creature_amount=1, hectare_number=tuple(hectare_number))
        elif lower_creature_type_command == "--boar" or lower_creature_type_command == "-bo":
            ecosystem.fill_creatures("boar", creature_amount=1, hectare_number=tuple(hectare_number))
        elif lower_creature_type_command == "--elk" or lower_creature_type_command == "-e":
            ecosystem.fill_creatures("elk", creature_amount=1, hectare_number=tuple(hectare_number))
        elif lower_creature_type_command == "--wolf" or lower_creature_type_command == "-w":
            ecosystem.fill_creatures("wolf", creature_amount=1, hectare_number=tuple(hectare_number))
        elif lower_creature_type_command == "--bear" or lower_creature_type_command == "-be":
            ecosystem.fill_creatures("bear", creature_amount=1, hectare_number=tuple(hectare_number))
        else:
            lower_creature_type_command = (f"Unknown type of creatures: {creature_type_command}. Input type of creature"
                                           f" again! (Use command \"help\" to get clarification):\t").lower()
            wrong_command = True


def remove_creature_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    creature_id = input("Input the id of creature to remove it:\t")
    lower_creature_id = creature_id.lower()
    ecosystem.remove_creature(lower_creature_id)
    os.system("clear")
    print(ecosystem)
    print(f"Creature \"{creature_id}\" was removed.")


def wake_deadly_worm_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    ecosystem.provoke_deadly_worm()
    os.system("clear")
    print(ecosystem)
    print("Deadly worm did his job.")


def apocalypse_command(ecosystem: EcoSystem, ecosystem_exists_flag) -> NoReturn:
    if not ecosystem_exists_flag:
        raise TypeError("EcoSystem doesn't exists")
    ecosystem.apocalypse()
    os.system("clear")
    print(ecosystem)
    print("Now You're become Death, the destroyer of worlds!")


def define_command(command: str, ecosystem=None) -> [EcoSystem, None]:
    if not ecosystem:
        ecosystem_exists_flag = False
    elif isinstance(ecosystem, EcoSystem):
        ecosystem_exists_flag = True
    else:
        raise TypeError(f"Unknown type of ecosystem: {type(ecosystem)}")
    lower_command = command.lower()
    if lower_command == "help":
        help_command()
    elif lower_command == "start new game" or lower_command == "start game" or lower_command == "start":
        ecosystem = start_command(ecosystem, ecosystem_exists_flag)
        print(ecosystem)
    elif lower_command == "exit game" or lower_command == "exit":
        exit_command(ecosystem, ecosystem_exists_flag)
    elif lower_command == "save game" or lower_command == "save":
        filename = save_command(ecosystem, ecosystem_exists_flag)
        print(f"Game saved to file \"{filename}\".")
    elif lower_command == "load game" or lower_command == "load":
        ecosystem = load_command(ecosystem, ecosystem_exists_flag)
        os.system("clear")
        print(ecosystem)
    elif lower_command == "period":
        period_command(ecosystem, ecosystem_exists_flag)
    elif lower_command == "creature stats":
        creature_stats_command(ecosystem, ecosystem_exists_flag)
    elif lower_command == "add creature" or lower_command == "add":
        add_creature_command(ecosystem, ecosystem_exists_flag)
    elif lower_command == "remove creature" or lower_command == "remove":
        remove_creature_command(ecosystem, ecosystem_exists_flag)
    elif lower_command == "wake deadly worm" or lower_command == "deadly worm":
        wake_deadly_worm_command(ecosystem, ecosystem_exists_flag)
    elif lower_command == "apocalypse":
        apocalypse_command(ecosystem, ecosystem_exists_flag)
    else:
        print(f"Unknown command: {command}")
        raise GameEndedException(exit_code=ExitCodes.REMOVABLE_INPUT_ERROR)
    return ecosystem


def play_console() -> int:
    sharps = "#" * 70
    print(f"{sharps}\n\nHello there! This is a simulation of ecosystem version {VERSION}\n\n{sharps}")
    ecosystem = None
    while True:
        try:
            command = input("Input command (input \"help \" to get clarification):\t")
            ecosystem = define_command(command=command, ecosystem=ecosystem)
        except ValueError as ver:
            print(f"ERROR!\n{ver.args[0]}")
            return ExitCodes.ERROR_INCORRECT_VALUE.value
        except TypeError as ter:
            print(f"ERROR!\n{ter.args[0]}")
            return ExitCodes.ERROR_UNKNOWN_TYPE_OF_PARAMETER.value
        except GameEndedException as stop:
            if stop.exit_code == ExitCodes.REMOVABLE_INPUT_ERROR:
                print("Use command \"help\" to get clarification")
                continue
            elif stop.exit_code == ExitCodes.NORMAL_END_NOT_SAVED or\
                    stop.exit_code == ExitCodes.NORMAL_END_SAVED or\
                    stop.exit_code == ExitCodes.WARNING_END_LOST_SAVED:
                print(stop.message)
            return stop.exit_code.value

