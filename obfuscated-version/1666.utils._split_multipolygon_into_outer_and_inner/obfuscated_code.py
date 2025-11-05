def extract_poly_coords(var_0):
    if var_0.type == 'Polygon':
        var_1 = var_0.exterior.coords[:]
        var_2 = []
        for interior in var_0.interiors:
            var_2 += interior.coords[:]
    elif var_0.type == 'MultiPolygon':
        var_1 = []
        var_2 = []
        for part in var_0:
            var_3 = extract_poly_coords(part)  # Recursive call
            var_1 += var_3['exterior_coords']
            var_2 += var_3['interior_coords']
    else:
        raise ValueError('Unhandled geometry type: ' + repr(var_0.type))
    return {'exterior_coords': var_1,
            'interior_coords': var_2}
