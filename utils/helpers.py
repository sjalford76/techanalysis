import numpy

def nanarray( n ):
    arr = numpy.empty( n )
    arr.fill(numpy.nan)
    return arr