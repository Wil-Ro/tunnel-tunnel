from enum import Enum

from display import Display
from input import Input
from level import Level
from player_stats import PlayerStats
from tunnel import Tunnel


class State(Enum):
    GUESSING = 0
    REVEALED = 1

class LevelRunner:


    def __init__(self, disp: Display, inp: Input, player: PlayerStats):
        self.disp = disp
        self.inp = inp
        self.state = State.GUESSING
        self.player = player

    def reveal(self):
        self.state = State.REVEALED

    def move_to_next_step(self, tunnel: Tunnel, level: Level):
        tunnel.append_step(level.get_next_step())
        self.state = State.GUESSING


    def run_level(self, level: Level, level_number: int):
        tunnel = Tunnel()
        self.player.lives = 10

        while True:
            self.disp.new_frame()

            if self.player.is_dead():
                return 0
            if level.steps >= level.length:
                return 1

            self.disp.display_lives(self.player.lives)
            self.disp.display_steps(level.steps, level.length)
            self.disp.display_level(level_number)


            match self.state:
                case State.GUESSING:
                    self.disp.darkness_revealed = False
                    self.disp.display_tunnel(tunnel)
                    self.disp.display_frame()

                    guesses_correct = self.inp.wait_on_key(tunnel.next_step.key)
                    if not guesses_correct:
                        self.player.lose_life()
                    else:
                        # self.player.heal_life()
                        pass

                    self.reveal()

                case State.REVEALED:
                    self.disp.darkness_revealed = True
                    self.disp.display_tunnel(tunnel)
                    self.disp.display_frame()

                    self.inp.wait_on_any_key() # wait on any key
                    self.move_to_next_step(tunnel, level)