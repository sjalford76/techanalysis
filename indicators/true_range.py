import numpy
from indicators.average import wilder_average

def true_range(highs, lows, closes):
    arr = numpy.empty(len(highs))
    arr[0] = highs[0] - lows[0]

    for i in range(1,len(highs)):
        arr[i] = max( abs(highs[i] - closes[i-1]), abs(lows[i] - closes[i-1] ), highs[i] - lows[i] )

    return arr

def atr(highs, lows, closes, n):

    tr = true_range(highs, lows, closes)

    return wilder_average(tr, n)
