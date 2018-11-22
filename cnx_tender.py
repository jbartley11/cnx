import arcpy
import datetime
import os


gdb = r"C:\Users\jaso9356\Documents\ArcGIS\Projects\cnx\cnx.gdb"
tracks = os.path.join(gdb, "LocationTracking")

# get user names and unique dates
users = set()
dates = set()

with arcpy.da.SearchCursor(tracks, ['Creator', 'CreationDate']) as cursor:
    for row in cursor:
        users.add(row[0])
        dates.add(row[1].date())


print(dates)
print(users)



# Get data
# Get earliest date
# Get all usernames
# For each date, query to check if worker has values or not
# Cluster - name date_worker save to filegdb
# Read cluster data
# Get start and stop times ?logic to cap time
# Start time - after first cluster or first point at expected time
# Get centroid
# Add to event layer
# Schema - date, event type, user, start, stop, duration, location