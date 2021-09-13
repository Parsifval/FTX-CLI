import ftx
from config import API_KEY, API_SECRET

client = ftx.FtxClient(api_key=API_KEY, api_secret=API_SECRET)

def main():
    dashboard()
    user_input = input('Enter a command: ')

    if 'orders' in user_input:
        open_orders()

    elif 'trade' in user_input:
        place_order()
        
    elif 'positions' in user_input:
        get_positions()

    elif 'price' in user_input:
        user_input = user_input.replace('price ', '')
        get_price(user_input)

def dashboard():
    print()

    assets_in_dashboard = ['BTC-PERP', 'ETH-PERP', 'ADA-PERP', 'BNB-PERP', 'SOL-PERP', 'XRP-PERP']

    for i in assets_in_dashboard:
        market = client.get_market(i)
        print(f"{i}: {market['price']}$")

def open_orders():
    print()
    orders = client.get_open_orders()

    i = 0
    try:
        while True:
            print(f"{i}) Market: {orders[i]['market']}, Status: {orders[i]['status']}, Side: {orders[i]['side']}, Size: {orders[i]['size']}, Side: {orders[i]['side']}")
            i += 1

    except IndexError:
        pass

    main()

def get_positions():
    print()
    positions = client.get_positions()

    i = 0
    try:
        while True:
            market = positions[i]
            if market['size'] == 0:
                pass
            else:
                print(f"Market: {market['future']}, Side: {market['side']}, Size: {market['cost']}, P/L: {market['unrealizedPnl']}, Breakeven price: {market['recentBreakEvenPrice']}")
            i += 1

    except IndexError:
        pass

    main()

def place_order():
    print()

    market = input('Market: ')
    side = input('Side: ')
    price = float(input('Price: '))
    size = float(input('Size '))

    client.place_order(market, side, price, size)

    main()

def get_price(market):
    print()

    try:
        price = client.get_market(market)
        print(f"{price['name']}: {price['price']}, 24 Hour Change: {price['change24h'] * 100}%")

    except:
        print('That market does not exist')

    main()


main()
