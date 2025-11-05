const isClockwise = (vertices=[]) => {
    const len = vertices.length;
    const sum = vertices.map(({x, y}, index) => {
        let nextIndex = index + 1;
        if (nextIndex === len) nextIndex = 0;

        return {
            x1: x,
            x2: vertices[nextIndex].x,
            y1: x,
            y2: vertices[nextIndex].x
        }
    }).map(({ x1, x2, y1, y2}) => ((x2 - x1) * (y1 + y2))).reduce((a, b) => a + b);

    if (sum > -1) return true;
    if (sum < 0) return false;
}
