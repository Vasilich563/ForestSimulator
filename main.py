#Author Vodohleb04

import sys
from console_mode import play_console
from game_main_window_gui import play_graphic_mode


def main(*args):
    """Starts Forest Simulator

    Possible args:
        --console | -c - starts game in console mode
        --graphic | - g - starts game in graphical mode
    """
    print(args)
    if not len(args) == 2:
        raise ValueError(f"Unknown arguments: {args}")
    if args[1] == "--concole" or args[1] == "-c":
        res = play_console()
        print(f"Game ended with exit code {res}")
        input()
    elif args[1] == "--graphic" or args[1] == "-g":
        play_graphic_mode()
    else:
        raise ValueError(f"Unknown args: {args}")


if __name__ == "__main__":
    main(*sys.argv)
