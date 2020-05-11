from app.bowling.frame_score_keeper import ScoringFrame
from app.bowling.bowling_utils import BowlingUtils


class Player:

    def __init__(self, name):
        self.name = name
        self.all_frames = {}
        self.current_score = 0
        self.current_round = 0

    def play_frame(self):
        bu = BowlingUtils()
        sr = ScoringFrame()
        sr.add_bowl(bu.parse_score_input("Pins knocked down on first bowl:", sr.get_pins_downed()))
        while sr.has_next():
            sr.add_bowl(bu.parse_score_input("Pins knocked down on next bowl:", sr.get_pins_downed()))
        self.all_frames[self.current_round] = sr
        if self.current_round == 9 and (sr.is_strike() or sr.is_spare()):
            sr_extra_one = ScoringFrame()
            sr_extra_one.add_bowl(bu.parse_score_input("Pins knocked down on next bowl:", sr_extra_one.get_pins_downed()))
            self.all_frames[self.current_round + 1] = sr_extra_one
            if not sr_extra_one.is_strike():
                sr_extra_one.add_bowl(bu.parse_score_input("Pins knocked down on next bowl:", sr_extra_one.get_pins_downed()))
            else:
                sr_extra_extra_one = ScoringFrame()
                sr_extra_extra_one.add_bowl(bu.parse_score_input("Pins knocked down on first bowl:", sr_extra_extra_one.get_pins_downed()))
                self.all_frames[self.current_round + 2] = sr_extra_extra_one
        self.current_round += 1

    def manage_round(self):
        """
        Runs and manges the entire round for the player.
        """
        print("Player {} is up to bowl!".format(self.name))
        self.play_frame()
        self.update_score()

    def update_score(self):
        """
        Calculates score from all complaete rouds
        """
        number_of_rounds = self.current_round
        score = 0
        for i in range(0, number_of_rounds):
            frame = self.all_frames.get(i)
            score += frame.get_pins_downed()
            next_round = self.all_frames.get(i + 1)
            next_next_round = self.all_frames.get(i + 2)
            if next_round is not None and (frame.is_strike() or frame.is_spare()):
                score += next_round.first_pins_downed
                if frame.is_strike() and not next_round.is_strike():
                    score += next_round.second_pins_downed
            if next_next_round is not None and (frame.is_strike() and next_round.is_strike()):
                score += next_next_round.first_pins_downed
        self.current_score = score
