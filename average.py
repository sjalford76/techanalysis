import numpy
import helpers

def rolling_average(srs, n):
    c = numpy.cumsum(srs, dtype=float)
    res = helpers.nanarray(len(srs))
    res[n:] = (c[n:]- c[:-n]) / n
    return res

def wilder_average(tr, n):
    result = helpers.nanarray(len(tr))
    result[n-1] = sum(tr[:n])/n
    
    for i in range(n, len(tr)):
        result[i] = ((n-1)*result[i-1] + tr[i])/n

    return result