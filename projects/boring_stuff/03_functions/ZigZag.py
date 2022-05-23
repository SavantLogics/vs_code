#Automate the Boring Stuff with Python

import time, sys
indent = 0 # How many spaces to indent
indent_Increasing = True # Whether the indentation is increasing or not

try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second

        if indent_Increasing:
            indent = indent + 1
            if indent == 20:
                indent_Increasing = False

        else:
            indent = indent - 1
            if indent == 0:
                indent_Increasing = True
except KeyboardInterrupt():
    sys.exit()