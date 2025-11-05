def test_distance_to_other_point(self):
    # Parametrize test with multiple cases:
    segments_and_point_and_answer = [
        [Segment(Point(1.0, 1.0), Point(1.0, 3.0)), Point(2.0, 4.0), math.sqrt(2.0)],
        [Segment(Point(1.0, 1.0), Point(1.0, 3.0)), Point(2.0, 3.0), 1.0],
        [Segment(Point(0.0, 0.0), Point(0.0, 3.0)), Point(1.0, 1.0), 1.0],
        [Segment(Point(1.0, 1.0), Point(3.0, 3.0)), Point(2.0, 2.0), 0.0],
        [Segment(Point(-1.0, -1.0), Point(3.0, 3.0)), Point(2.0, 2.0), 0.0],
        [Segment(Point(1.0, 1.0), Point(1.0, 3.0)), Point(2.0, 3.0), 1.0],
        [Segment(Point(1.0, 1.0), Point(1.0, 3.0)), Point(2.0, 4.0), math.sqrt(2.0)],
        [Segment(Point(1.0, 1.0), Point(-3.0, -3.0)), Point(-3.0, -4.0), 1],
        [Segment(Point(1.0, 1.0), Point(-3.0, -3.0)), Point(-4.0, -3.0), 1],
        [Segment(Point(1.0, 1.0), Point(-3.0, -3.0)), Point(1, 2), 1],
        [Segment(Point(1.0, 1.0), Point(-3.0, -3.0)), Point(2, 1), 1],
        [Segment(Point(1.0, 1.0), Point(-3.0, -3.0)), Point(-3, -1), math.sqrt(2.0)],
        [Segment(Point(1.0, 1.0), Point(-3.0, -3.0)), Point(-1, -3), math.sqrt(2.0)],
        [Segment(Point(-1.0, -1.0), Point(3.0, 3.0)), Point(3, 1), math.sqrt(2.0)],
        [Segment(Point(-1.0, -1.0), Point(3.0, 3.0)), Point(1, 3), math.sqrt(2.0)],
        [Segment(Point(1.0, 1.0), Point(3.0, 3.0)), Point(3, 1), math.sqrt(2.0)],
        [Segment(Point(1.0, 1.0), Point(3.0, 3.0)), Point(1, 3), math.sqrt(2.0)]
    ]

    for i, (segment, point, answer) in enumerate(segments_and_point_and_answer):
        result = segment.shortest_dist_to_point(point)
        self.assertAlmostEqual(result, answer, delta=0.001, msg=str((i, segment, point, answer)))
