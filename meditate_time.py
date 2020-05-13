# A program that fires up a youtube video periodically

import webbrowser
import time

daily_breaks = 3
breaks_count = 0
print ("The program lanched at :" + time.ctime())
while (breaks_count < daily_breaks):
    time.sleep(0.5)
    webbrowser.open('https://www.youtube.com/watch?v=iebciuBXCh4')
    breaks_count = breaks_count + 1
