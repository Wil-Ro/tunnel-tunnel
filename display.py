import curses
from _curses import A_DIM, A_BLINK, A_STANDOUT, A_BOLD
from curses import initscr

from tunnel import Tunnel


class Display:
    def __init__(self, scr):
        self.scr = scr
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        self.darkness_revealed = False

    def teardown_curses(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def new_frame(self):
        self.scr.clear()

    def display_frame(self):
        self.scr.refresh()

    def display_lose_screen(self):
        self.scr.addstr(2, 2, "the small creature died")
        self.scr.addstr(3, 2, "the tunnel was empty again")
        self.scr.addstr(4, 2, "any key to exit")
        self.scr.addstr(6, 13, " \\_")
        self.scr.addstr(7, 13, "⩍  \\ ")

    def display_win_screen(self):
        self.scr.addstr(2, 2, "the small creature explored the whole tunnel")
        self.scr.addstr(3, 2, "they had a nice time and were ready to go find another")
        self.scr.addstr(4, 2, "but first they wanted to sleep")
        self.scr.addstr(5, 2, "any key to exit")

        self.scr.addstr(7, 8, "Z")
        self.scr.addstr(8, 7, "zᶻ")
        self.scr.addstr(9, 5, "> ᶻ")



    # tunnel is 15 long
    def display_tunnel(self, tunnel: Tunnel):
        player_pos = 15
        y = 3
        x = 2

        self.scr.addstr(y, x, tunnel.get_as_str(), A_DIM)
        self.scr.addch(y, x+player_pos, ">")

        if self.darkness_revealed:
            self.scr.addch(y, x+player_pos+1, tunnel.next_step.char)
        else:
            self.scr.addch(y, x+player_pos+1, "▓", A_DIM)

        self.scr.refresh()

    def display_lives(self, lives):
        lives_string = "lives: " + ("v"*lives)
        self.scr.addstr(1, 2, lives_string, A_DIM)

    def display_level(self, level):
        self.scr.addstr(6, 2, "level: " + str(level), A_DIM)

    def display_steps(self, steps, total_steps):
        lives_string = "steps: " + str(steps) + "/" + str(total_steps)
        self.scr.addstr(5, 2, lives_string, A_DIM)

    def display_next_level(self):
        self.scr.addstr(2, 2, "The tunnel continues")
        self.scr.addstr(3, 2, "deeper to the next level")

        self.scr.addstr(5, 12, "⩍")


    def display_menu_art(self):
        self.scr.addstr(1, 13, " \\_")
        self.scr.addstr(2, 13, "⩍  \\  <")

        self.scr.addstr(4, 2, "A small creature")
        self.scr.addstr(4, 19, "explores", A_BOLD)
        self.scr.addstr(4, 28, "a tunnel")

    def display_menu(self, options, index):
        y = 7
        x = 13
        for i, option in enumerate(options):
            if i == index:
                self.scr.addstr(y+i, x-1, ">")
                self.scr.addstr(y+i, x, option)
            else:
                self.scr.addstr(y+i, x, option, A_DIM)



# ---o---o---o->-▓
