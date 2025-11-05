_nu = numpy.linalg.norm(u)
_nv = numpy.linalg.norm(v)
2.0 * numpy.arctan2( numpy.linalg.norm( u * _nv - v * _nu),
                     numpy.linalg.norm( u * _nv + v * _nu))
