from random import randint as ri
from pathlib import Path
from time import sleep
from app.bowling.player import Player
from app.bowling.bowling_utils import BowlingUtils


class DriverBowlingGame:

    def __init__(self):
        self.players = []

    def play_game(self):
        """
        Starts and runs the full game
        """
        self.get_welcome_screen()
        self.create_players()
        self.start_game()

    def create_players(self):
        bu = BowlingUtils()
        player_count = bu.parse_int_input("Enter the number of players:")
        for i in range(0, int(player_count)):
            name = bu.parse_input(input("Enter name for player {}. Leave blank to get random name:".format(i + 1)))
            if len(name) == 0:
                name = self.get_random_name()
            print("Name for player {} = {}".format(i + 1, name))
            self.players.append(Player(name))

    @staticmethod
    def get_random_name():
        """
        Gets random first and last names from the files
        """
        path_first_names = Path.joinpath(Path(__file__).absolute().parents[1], 'resources/bowling_first_names.txt')
        first_names = []
        with open(path_first_names.absolute()) as ffn:
            for line in ffn:
                first_names.append(str(line).replace("\n", ""))
        path_last_names = Path.joinpath(Path(__file__).absolute().parents[1], 'resources/bowling_last_names.txt')
        last_names = []
        with open(path_last_names.absolute()) as fln:
            for line in fln:
                last_names.append(str(line).replace("\n", ""))
        random_first = ri(0, len(first_names) - 1)
        random_last = ri(0, len(last_names) - 1)
        return "{} {}".format(first_names[random_first], last_names[random_last])

    @staticmethod
    def get_welcome_screen():
        path_welcome = Path.joinpath(Path(__file__).absolute().parents[1], 'resources/welcome_ascii.txt')
        with open(path_welcome.absolute()) as f:
            for line in f:
                print(str(line).replace("\n", ""))
                sleep(0.1)

    def start_game(self):
        print("Now starting the game!!!")
        for i in range(0, 10):
            print("Round {} Begins".format(i + 1))
            for p in self.players:
                p.manage_round()
                print("Player {} now has a score of {}".format(p.name, p.current_score))
            print("")


if __name__ == '__main__':
    dbg = DriverBowlingGame()
    dbg.play_game()
