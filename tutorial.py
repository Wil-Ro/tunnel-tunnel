from time import sleep

from enemy import Goblin, Empty
from level import level_lib
from level_runner import LevelRunner
from player_stats import PlayerStats
from tunnel import Tunnel


def tutorial(disp, inp):
    tunnel = Tunnel()

    disp.new_frame()
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(4, 17, "^ this is you")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(2, 18, "v its dark, you cant see whats infront of you")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(2, 18, "v hit space to reveal the next step")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.darkness_revealed = True
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(2, 18, "v hit space again to move forwards")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.darkness_revealed = False
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(2, 18, "v this next step has an enemy in it")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(2, 18, "v this enemy is an o, hit that key to handle it")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.darkness_revealed = True
    tunnel.append_step(Goblin())
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(2, 18, "v there we go! hit space to step forward again")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.darkness_revealed = False
    tunnel.append_step(Empty())
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(4, 18, "^ beware that you'll step forward automatically after a second")
    disp.scr.addstr(5, 18, "  ain't no time for dawdlin' in the tunnels!")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    disp.display_tunnel(tunnel)
    disp.scr.addstr(9, 2, "Enter to continue >")
    disp.scr.addstr(5, 2, "recognise the pattern, predict the enemies and handle them")
    disp.scr.addstr(6, 2, "you'll lose a few lives to start with, but you'll pick it up quickly")
    disp.scr.addstr(7, 2, "survive 40 steps to complete a level")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()

    disp.new_frame()
    level_runner = LevelRunner(disp, inp, PlayerStats())
    level_runner.run_level(level_lib.get_level(0), 0)

    disp.new_frame()
    disp.scr.addstr(2, 2, "You got this! Go explore the real tunnels now!")
    disp.display_frame()

    sleep(0.5)
    inp.wait_indefinitely_for_key()


