>> palmyra = LatLon(Latitude(5.8833), Longitude(-162.0833)) # Location of Palmyra Atoll in decimal degrees
>> palmyra = LatLon(5.8833, -162.0833) # Same thing but simpler! 
>> palmyra = LatLon(Latitude(degree = 5, minute = 52, second = 59.88),
                     Longitude(degree = -162, minute = -4.998) # or more complicated!
>> print palmyra.to_string('d% %m% %S% %H') # Print coordinates to degree minute second
('5 52 59.88 N', '162 4 59.88 W')`
