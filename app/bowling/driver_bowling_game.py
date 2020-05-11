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
        self.exit_screen()

    def create_players(self):
        bu = BowlingUtils()
        player_count = bu.parse_int_input("Enter the number of players:")
        for i in range(0, int(player_count)):
            name = bu.parse_input(input("Enter name for player {}. Leave blank to get random name:".format(i + 1)))
            if len(name) == 0:
                name = bu.get_random_name()
            print("Name for player {} = {}".format(i + 1, name))
            self.players.append(Player(name))

    @staticmethod
    def get_welcome_screen():
        path_welcome = Path.joinpath(Path(__file__).absolute().parents[1], 'resources/welcome_ascii.txt')
        with open(path_welcome.absolute()) as f:
            for line in f:
                print(str(line).replace("\n", ""))
                sleep(0.1)

    def start_game(self):
        """
        Runs the loop for the bowling portion of the game
        :return:
        """
        print("Now starting the game!!!")
        print("")
        for i in range(0, 10):
            print("Round {} Begins".format(i + 1))
            for p in self.players:
                p.manage_round()
                print("Player {} now has a score of {}".format(p.name, p.current_score))
                print("")
            print("")

    def exit_screen(self):
        max_score = -1
        winning_player = ""
        for p in self.players:
            score = p.current_score
            if score > max_score:
                max_score = score
                winning_player = p.name
        print("Game Complete! Winner is {} with a score of {}".format(winning_player, max_score))
        pass


if __name__ == '__main__':
    dbg = DriverBowlingGame()
    dbg.play_game()
