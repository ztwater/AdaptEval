<?php

use PhpGeoMath\Model\GeoSegment;
use PhpGeoMath\Model\Polar3dPoint;

$polarPoint1 = new Polar3dPoint(
    40.758742779050706, -73.97855507715238, Polar3dPoint::EARTH_RADIUS_IN_METERS
);

$polarPoint2 = new Polar3dPoint(
    40.74843388072615, -73.98566565776102, Polar3dPoint::EARTH_RADIUS_IN_METERS
);

$polarPoint3 = new Polar3dPoint(
    40.74919365249446, -73.98133456388013, Polar3dPoint::EARTH_RADIUS_IN_METERS
);

$arcSegment = new GeoSegment($polarPoint1, $polarPoint2);
$nearestPolarPoint = $arcSegment->calcNearestPoint($polarPoint3);

// Shortest distance from point-3 to segment(point-1, point-2)
$geoDistance = $nearestPolarPoint->calcGeoDistanceToPoint($polarPoint3);
