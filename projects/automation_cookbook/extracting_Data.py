from datetime import datetime
import delorean
from decimal import Decimal
from pytz import timezone

# Enter log to parse 
log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCE: 1345 - PRICE: $09.99'

# Split the log into parts which are divided by (-)
divide_it =  log.split(' - ')
timestamp_string, _, product_string, price_string = divide_it

# Parse the timestamp into a datetime object
timestamp = delorean.parse(timestamp_string.strip('[]'))
product_id = int(product_string.split(':')[-1])

# Parse the price into a decimal type
price = Decimal(price_string.split('$')[-1])

# Put in native Python format
timestamp, product_id, price(delorean(datetime=datetime(2018, 5, 5, 11, 7, 12, 267897), timezone='UTC'), 1345, Decimal('9.99'))