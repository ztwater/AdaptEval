using System.Collections.Generic;
using System.Linq;
using System.Numerics;

namespace SolidworksAddinFramework.Geometry
{
    public static class PlanePolygon
    {
        /// <summary>
        /// Assumes that polygon is closed, ie first and last points are the same
        /// </summary>
       public static bool Orientation
           (this IEnumerable<Vector3> polygon, Vector3 up)
        {
            var sum = polygon
                .Buffer(2, 1) // from Interactive Extensions Nuget Pkg
                .Where(b => b.Count == 2)
                .Aggregate
                  ( Vector3.Zero
                  , (p, b) => p + Vector3.Cross(b[0], b[1])
                                  /b[0].Length()/b[1].Length());

            return Vector3.Dot(up, sum) > 0;

        } 

    }
}
