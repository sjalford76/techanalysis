
class LongTrailingStop(object):

    
    def __init__(self, price, stop_distance):
        self._stop = price - stop_distance
        self._stop_distance = stop_distance

    def is_stopped(self, price):
        return price <= self._stop

    def update_stop(self, price):
        self._stop = max(self._stop, price - self._stop_distance)

    def get_stop(self):
        return self._stop
    
    def to_dict(self):
        return dict(Stop=self._stop, StopDistance=self._stop_distance)