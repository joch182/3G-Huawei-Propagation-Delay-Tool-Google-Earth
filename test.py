import math
import numpy as np

R = 6378.1 #Radius of the Earth in Km
distance = 0.234
angle = 10
BW = 60
angleRad = math.radians(angle)

print('Math.Radians: ')
print(angleRad)
print('=======')
originLon = -74.1147
originLat = 4.69517


lat2 = math.asin(math.sin(originLat)*math.cos(distance/R) + math.cos(originLat)*math.sin(distance/R)*math.cos(angleRad))
lon2 = originLon + math.atan2(math.sin(angleRad)*math.sin(distance/R)*math.cos(originLat), math.cos(distance/R)-math.sin(originLat)*math.sin(lat2))

print(lat2)
print(lon2)
print('=======')

rlat = np.deg2rad(originLat)
rlon = np.deg2rad(originLon)
rbearing = np.deg2rad(angle)
rdistance = distance / R

lat2 = math.asin(math.sin(rlat)*math.cos(rdistance) + math.cos(rlat)*math.sin(rdistance)*math.cos(rbearing))

print(lat2)
print(np.rad2deg(lat2))
print('=======')