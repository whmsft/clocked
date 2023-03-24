import time
import ntplib
import win32api
from datetime import datetime, timezone

idx = 0
Client = ntplib.NTPClient()
server = 'time.windows.com'

while True:
    try:
        print("==", idx,"==")
        print("LOG: Requesting time from server:",server)
        response = Client.request(server, version=3)
        response.offset
        TIME=str(datetime.fromtimestamp(response.tx_time, timezone.utc))
        print("LOG: Setting system time to:", TIME)
        win32api.SetSystemTime(int(TIME[0:4]), int(TIME[5:7]), 0, int(TIME[8:10]), int(TIME[11:13]), int(TIME[14:16]), int(TIME[17:19])+5, 0)
        print("LOG: System time updated to:", win32api.GetSystemTime(), "\n")
        idx = idx+1
        time.sleep(600)
    except:
        print("LOG: Error, Maybe No Internet.\n")
        time.sleep(10)
