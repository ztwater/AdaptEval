function IsClockwise(feature)
{
    if(feature.geometry == null)
        return -1;

    var vertices = feature.geometry.getVertices();
    var area = 0;

    for (var i = 0; i < (vertices.length); i++) {
        j = (i + 1) % vertices.length;

        area += vertices[i].x * vertices[j].y;
        area -= vertices[j].x * vertices[i].y;
        // console.log(area);
    }

    return (area < 0);
}
