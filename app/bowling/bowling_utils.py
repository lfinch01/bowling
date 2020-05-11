import sys
from pathlib import Path
from random import randint as ri

class BowlingUtils:

    def parse_int_input(self, promp):
        """
        :param promp:String Expected
        :return: Integer value from user input
        """
        user_input = input(promp)
        self.parse_input(user_input)
        try:
            return_value = int(user_input)
        except ValueError:
            print("Could not convert input to an integer. Try again")
            return_value = self.parse_int_input(promp)
        return return_value

    def parse_score_input(self, promp, total_pins_downed):
        """
        :param promp: String expected
        :param total_pins_downed: Integer expected
        :return: Integer not to exceed 10 total pins
        """
        pins_downed = self.parse_int_input(promp)
        if (pins_downed + total_pins_downed) > 10:
            print("Pins downed exceeded the number of pins. Try again")
            pins_downed = self.parse_score_input(promp, total_pins_downed)
        return pins_downed

    def parse_input(self, user_input):
        """
        Exits with code 0 if input is -Q
        :param user_input:String from user input expected
        """
        if user_input == '-Q':
            self.exit_game()
        return user_input

    def exit_game(self):
        print("Till next time!")
        sys.exit(0)

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