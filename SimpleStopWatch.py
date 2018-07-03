#Author: OMKAR PATHAK
#This script helps to build a simple stopwatch application using Python's time module.
#在windows的pycharm中运行时发现不能捕获Ctrl + C 的按键中断，在命令行中可以

import time

print('Press ENTER to begin, Press Ctrl + C to stop')
while True:
    try:
        input() # For ENTER. Use raw_input() if you are running python 2.x instead of input()
        starttime = time.time()
        print('Started')
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time.time()
        print('Total Time:', round(endtime - starttime, 2),'secs')
        break
