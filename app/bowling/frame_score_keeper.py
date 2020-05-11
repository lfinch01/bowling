

class ScoringFrame:

    def __init__(self, pins_downed_first):
        if pins_downed_first > 10:
            print("First bowl exceeds total number of pins. Setting first pins downed = {}".format(10))
            # Would normally raise an exception, but decided this would be more fun in the game
            self.pins_downed_first = 10
        else:
            self.pins_downed_first = pins_downed_first
        self.pins_downed_second = 0
        self.bowls_taken = 1
        self.strike = self.pins_downed_first == 10

    def is_strike(self):
        return self.strike

    def is_spare(self):
        if not self.strike and self.bowls_taken == 2:
            return (self.pins_downed_first + self.pins_downed_second) == 10
        else:
            return False

    def has_next(self):
        if not self.strike:
            if self.bowls_taken < 2:
                return True
        else:
            return False

    def add_bowl(self, pins_downed_second):
        self.bowls_taken += 1
        if pins_downed_second + self.pins_downed_first > 10:
            print("Pins downed exceeds total number of pins. Setting pins downed = {}".format(10-self.pins_downed_first))
            # Would normally raise an exception, but decided this would be more fun in the game
            self.pins_downed_second = 10-self.pins_downed_first
        else:
            self.pins_downed_second = pins_downed_second

    def get_pins_downed(self):
        return self.pins_downed_first + self.pins_downed_second