# Roshan Timing
# Gives randomly the time when the rosh aegis was killed
# Write aegis timing, minimum and maximum Roshan respawn timing

from random import randint
import time

k = 0
x = 0
for x in range(10):
    print('Attempt ' + str(x + 1) + "/10")

    # RANDOM TIMER IN GAME
    a = randint(10, 70)
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

    timer_aegis = str('Aegis - ' + str(aegis_a) + bb)

    # MIN TIMER ROSHAN
    int_min_rosh = a + 8
    min_rosh = str('Min Timing Roshan - ' + str(int_min_rosh) + bb)

    # MAX TIMER ROSHAN
    int_max_rosh = a + 11
    max_rosh = str('Max Timing Roshan - ' + str(int_max_rosh) + bb)

    # Enter Aegis, min or max + Check
    c = 1
    d = str(str(aegis_a) + bb + ' ' + str(int_min_rosh) + bb + '-' + str(int_max_rosh) + bb)
    if c == 1:

        print('Time of Roshans death: ' + timer)
        cc = str(input('Aegis min-max Roshan : '))
        if cc == str(d):
            k += 1
            print('Everything is correct, you are well done :)' + '\n')
        else:
            print('You made a mistake   : ' + d + '\n')

# Result
if x == 9:
    print('Result: ' + str(k) + "/10")
    if 0 <= k <= 4:
        print('More practice = more experience')
    if 5 <= k <= 7:
        print('Nice, continue in the same movement')
    if 8 <= k <= 9:
        print('You so good, bro')
    if k == 10:
        print('I love Dota 2 ❤')

time.sleep(15)
