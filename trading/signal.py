import numpy

''' a crosses b from below '''
def cross_from_below(a, b):
    if any( [isinstance(a, list), isinstance(b, list)] ):
        raise TypeError( "Lists are unsupported" )

    diff = a - b
    return numpy.array( [ 1 if diff[i-1] < 0 and d > 0 else 0 for i, d in enumerate(diff)] )

''' a crosses b from above '''
def cross_from_above(a, b):
    if any( [isinstance(a, list), isinstance(b, list)] ):
        raise TypeError( "Lists are unsupported" )

    diff = a - b
    return numpy.array( [ 1 if diff[i-1] > 0 and d < 0 else 0 for i, d in enumerate(diff)] )