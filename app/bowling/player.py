from app.bowling.frame_score_keeper import ScoringFrame

class Player:

    def __init__(self, name):
        self.name = name
        self.all_frames = {}
        self.current_score = 0
        self.current_round = 0
        self.round_open = False
        self.frame_open = False

    def record_score(self, pins_downed):
        sr = ScoringFrame(pins_downed)
        while(sr.has_next()):
            next_bowl = int(input("Pins knocked down on next bowl:"))
            sr.add_bowl(next_bowl)
        self.all_frames[self.current_round] = sr
        if self.current_round == 9 and (sr.is_strike() or sr.is_spare()):
            next_bowl = int(input("Pins knocked down on next bowl:"))
            sr_extra_one = ScoringFrame(next_bowl)
            self.all_frames[self.current_round+1] = sr_extra_one
        if self.current_round == 9 and sr.is_strike():
            next_bowl = int(input("Pins knocked down on next bowl:"))
            sr_extra_extra_one = ScoringFrame(next_bowl)
            self.all_frames[self.current_round + 2] = sr_extra_extra_one
        self.current_round += 1

    def start_frame(self):
        print("Player {} is up to bowl!".format(self.name))
        self.record_score(int(input("Pins knocked down on first bowl:")))
        self.update_score()

    def update_score(self):
        number_of_rounds = self.current_round
        score = 0
        for i in range(0, number_of_rounds):
            frame = self.all_frames.get(i)
            score += frame.get_pins_downed()
            next_round = self.all_frames.get(i+1)
            next_next_round = self.all_frames.get(i+2)
            if next_round is not None and (frame.is_strike() or frame.is_spare()):
                score += next_round.get_pins_downed()
            if next_next_round is not None and frame.is_strike():
                score += next_next_round.get_pins_downed()
        self.current_score = score





