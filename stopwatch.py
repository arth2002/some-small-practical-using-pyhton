import os
import time

second = 0
minutes = 0
hour = 0
print("press ctrl + c to exit")
try:
    while True:
        print("stopwatch\n")
        print('\t\t\t\t  %d : %d : %d ' % (hour, minutes, second))
        time.sleep(1)
        second += 1
        if second == 60:
            second = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        os.system("cls")
        print("press ctrl + c to exit")
except KeyboardInterrupt:
    print("Programm Ends")
