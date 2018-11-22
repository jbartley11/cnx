from arcgis.gis import GIS
import pandas as pd

tracks_id = "619be0d131594c579132caf247802c15"

# gis object
gis = GIS(username = 'jason_cnx',
          password = 'Hokuflw71esri')

# get tracks layer
tracks_item = gis.content.get(tracks_id)
tracks_layer = tracks_item.layers[0]

# query for all features
track_features = tracks_layer.query(where="Creator = 'lss0wos_consol' And CreationDate > '2018-10-12 00:00:00' And CreationDate < '2018-10-13 00:00:00'", out_fields="*")

# check for features
print(len(track_features))

# convert to spatial dataframe

# Log into ArcGIS anonymously
g = GIS()
# Retrieve an item from ArcGIS Online from a known ID value
known_item = g.content.get("85d0ca4ea1ca4b9abf0c51b9bd34de2e")
known_item