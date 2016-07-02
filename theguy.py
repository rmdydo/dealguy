from dealguy import audio, switch
from time import sleep
from multiprocessing import Pool
import sys


path = "/home/pi/dealguy/"
switch_number = 26


def morale_boost():
    next_sound = audio.get_next_sound("moraleBoost")
    audio.play(path + next_sound["fileName"])


def closed():
    next_sound = audio.get_next_sound("closed")
    pool = Pool(processes=1)
    pool.apply_async(switch.toggle, [switch_number, next_sound["switchDelay"], next_sound["switchDuration"]])
    audio.play(path + next_sound["fileName"])


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "closed":
        closed()
    else:
        morale_boost()
