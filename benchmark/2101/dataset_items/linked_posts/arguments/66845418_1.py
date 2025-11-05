output = {"type": "FeatureCollection", "features": [ {"type": "Feature",  "geometry": {"type": "Point", "coordinates": [103.815381, 1.279109]}, "properties": {"temperature": 24, "marker-symbol": "park", "marker-color": "#AF4646"}},  {"type": "Feature",  "geometry":  {"type": "MultiLineString", "coordinates": [[[103.809297, 1.294906], [103.799445, 1.283906], [103.815381, 1.294906]]]}, "properties": {"temperature": 24, "stroke": "#AF4646"}}]}
m = folium.Map(location=[1.2791,103.8154], zoom_start=14)

StyledGeoJson(output).add_to(m)
m
