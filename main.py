# Roshan Timing
# Gives randomly the time when the Roshan was killed
# Write Aegis timing, minimum and maximum Roshan respawn timing

import random
from random import randint
import time
from colorama import Fore
from colorama import init

init(autoreset=True)

k = 0
x = 0

# Start program
for x in range(10):
    print('Attempt ' + str(x + 1) + "/10")

    # RANDOM TIMER IN GAME
    a = randint(10, 50)
    if a <= 9:
        aa = str('0' + str(a))
    else:
        aa = str(str(a))
    b = randint(0, 59)
    if b <= 9:
        bb = str('0' + str(b))
    else:
        bb = str(str(b))
    timer = str(aa + ':' + bb)

    # AEGIS TIMER
    aegis_a = a + 5
    if aegis_a <= 9:
        aegis_a = str('0' + str(aegis_a))
    else:
        aegis_a = str(aegis_a)
    b = randint(0, 59)

    # MIN TIMER ROSHAN
    int_min_rosh = a + 8

    # MAX TIMER ROSHAN
    int_max_rosh = a + 11

    # Enter Aegis, min or max + Check
    c = 1
    d = str(str(aegis_a) + bb + ' ' + str(int_min_rosh) + bb + '-' + str(int_max_rosh) + bb)
    if c == 1:
        print('Time of Roshans death: ' + timer)
        cc = str(input('Aegis min-max Roshan : '))
        if cc == str(d):
            k += 1
            print(Fore.GREEN + 'Well, all corect :) ' + '\033[39m' + ' : ' + d + '\n')
        else:
            print(Fore.RED + 'You made a mistake( ' + '\033[39m' + ' : ' + d + '\n')

# Result
if x == 9:
    print('RESULT: ' + str(k) + "/10")
    if 0 <= k <= 4:
        print(Fore.RED + 'More practice = more experience!')
    if 5 <= k <= 7:
        print(Fore.YELLOW + 'Nice, continue in the same movement')
    if 8 <= k <= 9:
        print(Fore.GREEN + 'You so good, bro')
    if k == 10:
        print(Fore.BLUE + 'I love Dota 2')

time.sleep(15)
