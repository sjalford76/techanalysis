import numpy
from helpers import nanarray

def rsi( data, n):
        diffs = numpy.empty( len(data) )
        diffs.fill(numpy.nan)
        diffs[1:] = numpy.diff(data)

        ups = numpy.array([ u if u >= 0 else 0 for u in diffs ])
        downs = numpy.array([ -1*d if d < 0 else 0 for d in diffs ])

        up_average = nanarray(len(data))
        down_average = nanarray(len(data))

        up_average[n] = sum(ups[:n+1])/n
        down_average[n] = sum(downs[:n+1])/n

        for i in range(n+1, len(data)):
                up_average[i] = ((n - 1)*up_average[i-1] + ups[i] )/ n
                down_average[i] = ((n - 1)*down_average[i-1] + downs[i] )/n

        #Step 7 5/6
        average_up_down = nanarray(len(data))
        average_up_down[n:] = numpy.divide(up_average[n:], down_average[n:] )

        #step 8
        rsi = 100.0 - 100 / ( average_up_down + numpy.ones(len(data)))

        return rsi



