import shapely

def _split_multipolygon_into_outer_and_inner(geom: shapely.MultiPolygon):  # type: ignore
    # https://stackoverflow.com/a/21922058
    exterior_coords = []
    interior_coords = []

    if geom.geom_type == "MultiPolygon":        
        for part in geom.geoms:
            epc = _split_multipolygon_into_outer_and_inner(part)  # Recursive call
            exterior_coords += epc[0]
            interior_coords += epc[1]
    elif geom.geom_type == "Polygon":
        exterior_coords = geom.exterior.coords[:]
        interior_coords = []
        for interior in geom.interiors:
            interior_coords += interior.coords[:]
    else:
        raise ValueError(f"Unhandled geometry type: {repr(geom.geom_type)}")
        #raise ValueError('Unhandled geometry type: ' + repr(geom.geom_type))

    return exterior_coords, interior_coords
