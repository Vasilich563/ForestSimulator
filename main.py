#Author Vodohleb04
from game import play_console

if __name__ == "__main__":
    res = play_console()
    print(f"Game ended with exit code {res}")
    input()


# TODO Help Dialog
# TODO Get Version from config!
# TODO Data controller
# TODO Make creature stats dialog name using id of creature
# TODO Hide gender and parents information of creature stats when dialog is called for plant
