
class ScoringFrame:

    def __init__(self):
        self.first_pins_downed = 0
        self.second_pins_downed = 0
        self.bowls_taken = 0

    def is_strike(self):
        if self.bowls_taken == 1 and self.first_pins_downed == 10:
            return True
        else:
            return False

    def is_spare(self):
        if self.bowls_taken == 2 and (self.first_pins_downed + self.second_pins_downed) == 10:
            return True
        else:
            return False

    def has_next(self):
        if not self.is_strike():
            if self.bowls_taken < 2:
                return True
        else:
            return False

    def add_bowl(self, pins_downed):
        if self.bowls_taken == 1:
            self.second_pins_downed = pins_downed
            self.bowls_taken = 2
        else:
            self.first_pins_downed = pins_downed
            self.bowls_taken = 1

    def get_pins_downed(self):
        return self.first_pins_downed + self.second_pins_downed

