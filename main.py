import curses
from curses import wrapper
from enum import Enum
from time import sleep

from enemy import KnifeRat
from input import Input
from level import Level, level_lib
from display import Display
from level_runner import LevelRunner
from player_stats import PlayerStats
from tunnel import Tunnel
from tutorial import tutorial


class App:
    def __init__(self, scr):
        self.disp = Display(scr)
        self.inp = Input(scr)


    def app(self):
        selected_item = 0
        menu_items = ["play", "tutorial", "quit"]
        while True:
            self.disp.new_frame()
            self.disp.display_menu_art()
            self.disp.display_menu(menu_items, selected_item)
            self.disp.display_frame()

            key =  self.inp.wait_on_any_key()
            if key == curses.KEY_UP or key == ord("w"):
                selected_item -= 1
                if selected_item < 0:
                    selected_item = len(menu_items)-1

            elif key == curses.KEY_DOWN or key == ord("s"):
                selected_item += 1
                if selected_item >= len(menu_items):
                    selected_item = 0

            elif key == ord("\n") or key == ord(" "):
                match menu_items[selected_item]:
                    case "play":
                        self.cycle_through_levels()
                    case "tutorial":
                        self.tutorial()
                    case "quit":
                        exit(0)


    def cycle_through_levels(self):
        stats = PlayerStats()
        level_runner = LevelRunner(self.disp, self.inp, stats)

        level_lib.current_level = 0
        for level in level_lib:
            score = level_runner.run_level(level, level_lib.current_level)
            if score == 0:
                self.defeat_screen()

            self.disp.display_next_level()
            self.inp.wait_indefinitely_for_key()
            self.inp.wait_indefinitely_for_key() # wait twice to debounce

        self.win_screen()

    def defeat_screen(self):
        self.disp.display_lose_screen()
        self.inp.wait_indefinitely_for_key()
        self.inp.wait_indefinitely_for_key() # wait twice to debounce

        exit(0)

    def win_screen(self):
        self.disp.display_win_screen()
        self.inp.wait_indefinitely_for_key()
        self.inp.wait_indefinitely_for_key() # wait twice to debounce

        exit(0)

    def tutorial(self):
        tutorial(self.disp, self.inp)










if __name__ == '__main__':
    def run(scr):
        app = App(scr)
        app.app()

    wrapper(run)

# todo fix fizzbuzz
# todo tutorial