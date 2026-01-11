
class Trade(object):
    
    def __init__(self, date, traded_price, size, stop = None, take_profit = None, expiry = None, exit_price = None, exit_date = None, trade_high=None, trade_low=None):
        self._date = date
        self._traded_price = traded_price
        self.size = size
        self._stop = stop
        self._take_profit = take_profit
        self._expiry = expiry
        self._exit_price = exit_price
        self._exit_date = exit_date
        self._trade_high = trade_high
        self._trade_low = trade_low
    
    @property
    def date(self):
        return self._date
    
    @property
    def traded_price(self):
         return self._traded_price
    
    @property
    def stop(self):
        return self._stop
    
    @property
    def take_profit(self):
        return self._take_profit
    
    @property
    def expiry(self):
        return self._expiry
    
    @property
    def exit_price(self):
        return self._exit_price
    
    @property
    def exit_date(self):
        return self._exit_date

    @property
    def trade_high(self):
        return self._trade_high
    
    @property
    def trade_low(self):
        return self._trade_low

    def set_exit_price(self, price):
        self._exit_price = price

    def set_exit_date(self, date):
        self._exit_date = date
    
    def set_trade_high(self, price):
        self._trade_high = price

    def set_trade_low(self, price):
        self._trade_low
    
    def set_stop(self, price):
        self._stop =price

    @staticmethod
    def to_dict(trade):
        return dict( Date=trade.date
                    , TradePrice=trade.traded_price
                    , Stop=trade.stop
                    , TakeProfit=trade.take_profit
                    , Expiry=trade.expiry
                    , ExitPrice=trade.exit_price
                    , ExitDate=trade.exit_date 
                    , TradeHigh=trade.trade_high
                    , TradeLow=trade.trade_low)