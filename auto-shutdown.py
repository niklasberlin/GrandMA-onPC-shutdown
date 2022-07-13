from time import sleep
import psutil
import time
import os


# the list the contain all process dictionaries
def checkStatus(pname):
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
            name = process.name()
            if(name==pname):
                return True
    return False


was_seen = False
while True:
    status = checkStatus("gma2onpc.exe")
    if(not was_seen and status):
        was_seen = True        
    if(was_seen and not status):
        os.system("shutdown /s /t 1")
    time.sleep(5) # sleep for 5 seconds