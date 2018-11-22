# import json
# json_string = "{'x': 1234561, 'y': 4531561}"
# json.loads(json_string)
# def return_x(json_string):
#     d = json.loads(json_string)
#     return d['x']

# print(return_x(json_string))

import sys
import arcgis
import widgetsnbextension
import ipywidgets
print("python version: ",sys.version)
print("arcgis API version: ",arcgis.__version__)
print("widgetnbextension: ",widgetsnbextension.__version__)
print("ipywidgets version: ",ipywidgets.__version__)
