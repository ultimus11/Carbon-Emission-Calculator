from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

# Lat & lON OF SOURCE AND DESTINATION
lat1 = radians(19.03314405429594)
lon1 = radians(73.01662301314084)
lat2 = radians(19.006484392933224)
lon2 = radians(73.02849371152573)

#DIFFERENCE 
dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Distance in KM:", distance)
print((distance*150)/1000,"Kilograms")