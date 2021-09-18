import ftx
from config import API_KEY, API_SECRET

client = ftx.FtxClient(api_key=API_KEY, api_secret=API_SECRET)

def main():
    print()
    user_input = input('Enter a command: ')

    if 'orders' in user_input:
        open_orders()

    elif 'trade' in user_input:
        user_input = user_input.replace('trade ', '')
        user_input_list = [user_input]
        order = ' '.join(user_input_list).split()
        place_order(order)
        
    elif 'positions' in user_input:
        get_positions()

    elif 'price' in user_input:
        user_input = user_input.replace('price ', '')
        get_price(user_input)

    elif 'dashboard' in user_input:
        dashboard()

    elif 'balances' in user_input:
        balances()

    elif 'help' in user_input:
        help()

def dashboard():
    print()

    account_info = client.get_account_info()
    collateral = (account_info['collateral'])
    free_collateral = account_info['freeCollateral']

    print(f'Account collateral: {collateral}$')
    print(f'Free collateral:    {free_collateral}$')

    main()

def balances():
    print()
    balances = client.get_balances()

    i = 0
    try:
        while True:
            balance = balances[i]

            if balance['total'] != 0:
                print(f"{balance['coin']}: {balance['total']}")

            i += 1
    
    except IndexError:
        pass

    main()

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
                print(f"Market: {market['future']}, Side: {market['side']}, Size: {market['cost']}$, P/L: {market['unrealizedPnl']}, Breakeven price: {market['recentBreakEvenPrice']}")
            i += 1

    except IndexError:
        pass

    main()

def place_order(order):
    print()

    try:
        market = order[0]
        side = order[1]
        price = float(order[2])
        size = float(order[3])
        print(f'{market}, {side}, {price}, {size}')

        client.place_order(market, side, price, size)

    except:
        print("The API was unable to fulfill your request. Enter the 'help' command to see how to properly submit an order using the CLI.")

    main()

def get_price(market):
    print()

    try:
        price = client.get_market(market)
        print(f"{price['name']}: {price['price']}, 24 Hour Change: {price['change24h'] * 100}%")

    except:
        print('That is not a valid market')

    main()

def help():
    print()
    print("To view your open orders enter: 'orders'.")
    print("To view your open positions enter: 'positions'")
    print("To get the price of an asset enter: 'price ASSET_TICKER'")
    print()
    print("To trade enter: trade ASSET_TICKER BUY_OR_SELL PRICE_YOU_WISH_TO_BUY_AT AMOUNT_OF_THE_ASSET_YOU_WISH_TO_BUY")
    print("For example, the following command will buy 1 BTC at a price of 50000$: 'trade BTC-PERP buy 50000 1'")

    main()
    
dashboard()
main()
