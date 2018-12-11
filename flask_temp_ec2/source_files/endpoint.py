from flask import jsonify
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import time
import json
import os
from subprocess import check_output
from datetime import datetime, timedelta

app = Flask(__name__)
api = Api(app)

# enable CORS
CORS(app)

epoch = time.time()
time_start = (datetime.now()-timedelta(hours=.5)).timestamp()
print(type(time_start))
time_end = datetime.now().timestamp()
print(type(time_end))

def get_temps():
    with open('./Temps/temp.json','r') as myfile:
        temperatures = json.load(myfile)
        print(temperatures)
        # temps = json.dumps(
        return temperatures
    # therm_list = [{x:y} for x in range(time_start, time_end)]


class Temp(Resource):
    def get(self):
        return get_temps(), 200
       # for item in temperatures:
       #     time_string = list(item)[0]
       #     print(time_string)
       #     print(type(time_string))
       #     if time_start < float(time_string) < time_end:
       #         return temperatures, 200
       # return 'Nothing Here', 404

#    def put(self, temp):
#         pass
#     def post(self, temp):
#         pass
#     def delete(self, temp):
#         pass
#
api.add_resource(Temp, '/temp')
app.run(host='0.0.0.0', debug=True)