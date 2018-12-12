import os
from subprocess import check_output
import schedule
import time

def get_s3_data():
    path = os.getcwd()
    if os.path.isdir('Temps') is False:
        os.mkdir(path+'/Temps')

    s3_copy = check_output(['aws', 's3', 'cp',
                            's3://semyonovtest/tempdata/temps.json',
                            path+'/Temps/temp.json'])

    videos = check_output(['aws', 's3', 'cp',
                            's3://semyonovtest/Videos',
                            path+'/Videos/', '--recursive'])
    print(videos)
    print(s3_copy)
    return s3_copy
getdata = get_s3_data()
print(getdata)
schedule.every(20).seconds.do(get_s3_data)
# schedule.every().day.at('08:00').do(get_s3_data)
# schedule.every().day.at('13:00').do(get_s3_data)
# schedule.every().day.at('18:00').do(get_s3_data)

while True:
    schedule.run_pending()
    time.sleep(10)

