dLon = lon2 - lon1;
y = Math.sin(dLon) * Math.cos(lat2);
x = Math.cos(lat1)*Math.sin(lat2) -
        Math.sin(lat1)*Math.cos(lat2)*Math.cos(dLon);
brng = Math.atan2(y, x).toDeg();
