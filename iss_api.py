# This software uses api from the "wheretheiss" website to locate the ISS relative to the user's position, showing the difference in latitude and longitude.
import requests
import json

# API keys and conversion to json
response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
response_2 = requests.get("Put your location API here")
res = response.json()
res_2 = response_2.json()

# Assigning variables to users coordinates and that of the ISS
iss_lat = float(res["latitude"])
my_lat = float(res_2["latitude"])
iss_long = float(res["longitude"])
my_long = float(res_2["longitude"])

# Method to calculate the difference in latitude

def latitude_conv(iss_lat, my_lat):
    diff_lat = 0
    if iss_lat > 0 and my_lat > 0:
        diff_lat = iss_lat - my_lat
    elif iss_lat < 0 and my_lat > 0:
        diff_lat = my_lat - iss_lat
    elif iss_lat > 0 and my_lat < 0:
        diff_lat = iss_lat - my_lat
    elif iss_lat < 0 and my_lat < 0:
        diff_lat = abs(iss_lat) - abs(my_lat)
    return abs(diff_lat)

# Method to calculate the difference in longitude

def longitude_conv(iss_long, my_long):
    diff_long = 0
    if iss_long > 0 and my_long > 0:
        diff_long = iss_long - my_long
    elif iss_long < 0 and my_long > 0:
        diff_long = my_long - iss_long
    elif iss_long > 0 and my_long < 0:
        diff_long = iss_long - my_long
    elif iss_long < 0 and my_long < 0:
        diff_long = abs(iss_long) - abs(my_long)

    if abs(diff_long) > 180:
        diff_long = 360 - abs(diff_long)
    return diff_long

print(res)
print(res_2)
if iss_lat == my_lat and iss_long == my_long:
    print("The ISS is directly over me!!")
print("Its still far away from you, you are at {} latitude, {} longitude, while the ISS is at {} lat, {} long".format(my_lat,my_long,iss_lat,iss_long))
