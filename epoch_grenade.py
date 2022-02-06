#
#   raspberry pi epoch counter V0.1
#   
#   Will continueously count up from the moment you run it
#   This is currently only a proof of concept
#
#   TODO: Add raspberry pi functionality
#   TODO: Compare config date modified to the epoch stored within it
#   TODO: Add date when activated

import calendar as c
import time as t
import os

epoch_time = 0  # current epoch time
start_time = 0  # when program was first run

# path of the configuration files; default is in the same directory.
# the only thing that is saved to this file is the epoch at the time of first run.
epoch_config_path = "epoch_grenade.conf"

# checks to see if a config file already exists
if os.path.exists(epoch_config_path):
    # reads the config file to "start_time" variable
    with open(epoch_config_path,"r") as file:
        try:
            start_time = int(file.read())
        except:
            print("Error reading value starting value. \
Try deleting 'epoch_grenade.conf'")
            exit()
else:
    # creates config file and writes current epoch
    with open(epoch_config_path, "w") as file:
        file.write(str(epoch_time))
    start_time = epoch_time

# just prints out the difference in epochs
# TODO: write to raspi screen
while True:
    epoch_time = int(t.time())
    print(epoch_time - start_time)
    t.sleep(1)