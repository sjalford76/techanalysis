import numpy
from helpers import nanarray
import average

def rsi( data, n):
        diffs = nanarray(len(data))
        diffs[1:] = numpy.diff(data)

        ups = numpy.array([ u if u >= 0 else 0 for u in diffs ])
        downs = numpy.array([ -1*d if d < 0 else 0 for d in diffs ])

        up_average = nanarray(len(data))
        down_average = nanarray(len(data))

        up_average = average.wilder_average(ups, n)
        down_average = average.wilder_average(downs, n)

        #Step 7 5/6
        average_up_down = nanarray(len(data))
        average_up_down[n:] = numpy.divide(up_average[n:], down_average[n:] )

        #step 8
        rsi = 100.0 - 100 / ( average_up_down + numpy.ones(len(data)))

        return rsi



