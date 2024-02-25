
class Trade(object):
    
    def __init__(self, date, traded_price, size, stop = None, take_profit = None, expiry = None, exit_price = None):
        self._date = date
        self._traded_price = traded_price
        self._stop = stop
        self._take_profit = take_profit
        self._expiry = expiry
        self._exit_price = exit_price
    
    def date(self):
        return self._date
    
    def traded_price(self):
         return self._traded_price
    
    def stop(self):
        return self._stop
    
    def take_profit(self):
        return self._take_profit
    
    def expiry(self):
        return self._expiry
    
    def exit_price(self):
        return self._exit_price
    
    def set_exit_price(self, price):
        self._exit_price = price
    
    @staticmethod
    def to_dict(trade):
        return dict( Date=trade.date()
                    , TradePrice=trade.traded_price()
                    , Stop=trade.stop()
                    , TakeProfit=trade.take_profit()
                    , Expiry=trade.expiry()
                    , ExitPrice=trade.exit_price() )