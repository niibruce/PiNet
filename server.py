import os
import time
import json


with open("schedule.json") as schedule:
    schedule = json.loads(schedule.read())
    
    if schedule['mode'] == 'repeat':
        current = 0
        while True:
            if current >= len(schedule['details']):
                current = 0
            
            current_asset = schedule['details'][current]
            asset_name = current_asset['asset']
            sleep_for = current_asset['sleep']
            CMD = "/usr/bin/uzbl-browser -c /home/pi/uzbl.conf /home/pi/Code/PiNet/assets/%s &" % asset_name
            os.system(CMD)
            time.sleep(sleep_for)
            CMD = "ps -ef | grep uzbl | cut -d' ' -f9 | xargs kill"
            os.system(CMD)
            current += 1
