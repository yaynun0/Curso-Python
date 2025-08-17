import datetime
import time,os

for i in range(100):
    os.system('cls')
    t=datetime.datetime.now()
    print("{}:{}:{}".format(t.hour,t.minute,t.second))
    time.sleep(1)
    i+=1
