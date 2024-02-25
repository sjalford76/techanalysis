import numpy
import helpers

def rolling_average(srs, n):
    c = numpy.cumsum(srs, dtype=float)
    res = helpers.nanarray(n)
    res[n:] = (c[n:]- c[:-n]) / n
    return res

def wilder_average(srs, n):
    result = helpers.nanarray(n)
    result[n-1] = sum(srs[:n])/n
    
    for i in range(n, len(srs)):
        result[i] = ((n-1)*result[i-1] + srs)/n

    return result