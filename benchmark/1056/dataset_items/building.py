# Import libraries

from shapely.geometry import Polygon
import numpy as np

 
def get_minimum_bounding_rectangle(building_nodes):
    """Helper function to generate minimum bounding rectangle around each Polygon.

    Args:
        building_nodes (gpd.GeoDataFrame): A geopandas GeoDataFrame corresponding to building footprints. 

    Returns:
        list: A list consisting of minimum bounding rectangles (shapely.geometry.Polygon) for each building footprint. 
    """    
    # Adapted and modified to work with gpd.GeoDataFrame input (Original algorithm:  https://stackoverflow.com/questions/13542855/algorithm-to-find-the-minimum-area-rectangle-for-given-points-in-order-to-comput answered by user JesseBuesking)
    
    from scipy.ndimage import rotate
    pi2 = np.pi/2
    
    # Get convex hull coordinates
    convex_hull_points = [np.array(i.coords) for i in building_nodes.convex_hull.exterior] 
    
    # Get vector between each point by subtraction
    edges = [point[1:] - point[:-1] for point in convex_hull_points]
    
    # Compute angle between vectors
    angles = [np.arctan2(edge[:, 1], edge[:, 0]) for edge in edges]
    angles = [np.abs(np.mod(angle, pi2)) for angle in angles]
    angles = [np.unique(angle) for angle in angles]
    
    mbr_list = []
    
    for angle, hull_coords in zip(angles, convex_hull_points):
        rotations = np.vstack([
                np.cos(angle),
                np.cos(angle-pi2),
                np.cos(angle+pi2),
                np.cos(angle)]).T

        rotations = rotations.reshape((-1, 2, 2))
        
        # apply rotations to the hull
        rot_points = np.dot(rotations, hull_coords.T)
        
        # find the bounding points
        min_x = np.nanmin(rot_points[:, 0], axis=1)
        max_x = np.nanmax(rot_points[:, 0], axis=1)
        min_y = np.nanmin(rot_points[:, 1], axis=1)
        max_y = np.nanmax(rot_points[:, 1], axis=1)
        
        # find the box with the best area
        areas = (max_x - min_x) * (max_y - min_y)
        best_idx = np.argmin(areas)
        
        # return the best box
        x1 = max_x[best_idx]
        x2 = min_x[best_idx]
        y1 = max_y[best_idx]
        y2 = min_y[best_idx]
        r = rotations[best_idx]

        rval = np.zeros((4, 2))
        rval[0] = np.dot([x1, y2], r)
        rval[1] = np.dot([x2, y2], r)
        rval[2] = np.dot([x2, y1], r)
        rval[3] = np.dot([x1, y1], r)
        
        mbr_list.append(Polygon(rval))
        
    return mbr_list
 
