import ftx
from config import API_KEY, API_SECRET

client = ftx.FtxClient(api_key=API_KEY, api_secret=API_SECRET)

def main():
    print()
    user_input = input('Enter a command: ')

    if 'open orders' in user_input:
        open_orders()

def open_orders():
    print()
    orders = client.get_open_orders()

    i = 0
    try:
        while True:
            print(f"{i}) Market: {orders[i]['market']}, Status: {orders[i]['status']}, Side: {orders[i]['side']}, Size: {orders[i]['size']}, Size (USD): {orders[i]['side']}")
            i += 1

    except IndexError:
        pass

main()
