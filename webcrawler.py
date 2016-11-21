

import ystockquote
import operator
import datetime

from datetime import date, timedelta


def getPrevClose(date):
#    dayofweek = datetime.datetime.strptime(date, "%y-%m-%d").strftime('%A')
    prev_day = datetime.datetime.strptime(date, "%y-%m-%d") - timedelta(1)
#    if (dayofweek == 'Monday'):
#        prev_day = prev_day - timedelta(2)

    key = '20' + prev_day.strftime('%y-%m-%d')
#    print ('Prev Day ' + key)

    if (key == '2014-12-31'):
        return False

    while not ( key in price_history.keys()):
        prev_day = datetime.datetime.strptime(prev_day, "%y-%m-%d") - timedelta(1)
        key = '20' + prev_day.strftime('%y-%m-%d')


    return price_history[key]['Close']




def getPriceHistory():
    yesterday = date.today() - timedelta(1)
    yesterday = '2016-' + yesterday.strftime('%m-%d')


    price_history = ystockquote.get_historical_prices('006400.KS', '2015-01-01', yesterday)
    return price_history



price_history = getPriceHistory()
sorted_keys = sorted(price_history.keys())

for key in sorted_keys:
    print "Date : " + key  + " "  + price_history[key]['Close']
    print getPrevClose(key[2:])

