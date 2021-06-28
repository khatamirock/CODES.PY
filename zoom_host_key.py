import itertools
import pyautogui
import pyperclip
import logging
import time
import timeit
import sys
from pynput.mouse import Button, Controller

pyautogui.FAILSAFE = True  # moving the cursor to the upper left corner of the screen will terminate the program.
mouse = Controller()

master_key = []


def generate_perms(digits):
    print('Creating key list...')
    combos = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                    repeat=digits))  # digits is the r value (10 for a 10 digit key etc.)
    print(combos)
    for i in combos:
        res = ''.join(str(x) for x in i)
        master_key.append(res)


    print(master_key)
nex = iter(master_key)  # turning the master list of all host keys into an iterator.