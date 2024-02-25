import pytest

from trading.trailing_stop import LongTrailingStop

def test_trailing_stop():

    stop = LongTrailingStop(100, 10)

    assert stop.get_stop() == 90.0

    stop.update_stop(105.0)

    assert stop.get_stop() == 95.0

    stop.update_stop(97.0)

    assert stop.get_stop() == 95.0

    stop.update_stop(106.0)

    assert stop.get_stop() == 96.0

    assert stop.is_stopped(107) == False

    assert stop.is_stopped(95) == True


