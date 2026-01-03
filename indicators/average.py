import numpy
import utils.helpers as helpers

def rolling_average(srs, n):
    c = numpy.cumsum(srs, dtype=float)
    res = helpers.nanarray(len(srs))
    res[n:] = (c[n:]- c[:-n]) / n
    return res

def wilder_average(tr, n, offset=0):
    result = helpers.nanarray(len(tr))
    result[n+offset-1] = sum(tr[offset:offset + n])/n
    
    for i in range(n + offset, len(tr)):
        result[i] = ((n-1)*result[i-1] + tr[i])/n

    return result