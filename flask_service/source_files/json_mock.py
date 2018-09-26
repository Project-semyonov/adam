import random
import json
from datetime import datetime, timedelta
import time

class create_json_file():
    def __init__(self):
        # self.epoch = datetime.now().timestamp()
        self.time_list = []
    def create_json(self):
        for x in range(0,10):
            temp_dict = {}
            temp = random.randint(84,99)
            temp_dict[str(datetime.now().timestamp())] = str(temp)
            time.sleep(random.randint(0,10))
            self.time_list.append(dict(temp_dict))
            print(str(self.time_list))
        with open('temperature.json', 'w') as file:
            # json_data = json.load(str(self.time_list))
            json.dump(self.time_list, file)



if __name__ == '__main__':


        myfile = create_json_file()
        myfile.create_json()


