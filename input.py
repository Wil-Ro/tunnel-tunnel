import curses
from curses import *



class Input:
    def __init__(self, scr):
        self.scr = scr
        halfdelay(10)

    def wait_on_any_key(self) -> int:
        try:
            key_given = self.scr.getch()
            return key_given
        except curses.error:
            pass

    def wait_on_key(self, key):
        try:
            key_given = self.scr.getch()
            if key_given is None:
                return False
            if key_given == ord(key):
                return True
        except curses.error:
            pass

        return False

    def wait_indefinitely_for_key(self):
        nocbreak()
        self.scr.getch()
        halfdelay(20)