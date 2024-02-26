from trading.signal import cross_from_below
import numpy

def test_cross_from_below():
    a = numpy.array([ 100.0, 110, 121, 130.0 ])
    b = numpy.array([ 110.0, 115.0, 120, 125 ])

    crosses = cross_from_below(a, b)
    assert crosses[0] == 0
    assert crosses[1] == 0
    assert crosses[2] == 1
    assert crosses[3] == 0
    
        