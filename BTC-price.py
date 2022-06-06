import requests 


def inform_holder():
    print('hi there, price is good ')

    
my_Good_price = 27000
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(response.json()['data']['amount'])


print('at this moment, bitcon is %i Dollors' % price)


if (price < my_Good_price):
    inform_holder()
