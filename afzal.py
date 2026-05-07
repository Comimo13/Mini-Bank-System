import json


def line():
    print('=============================================================================')

# noinspection PyBroadException
def deposit():
    try:
        amount = int(input('Enter amount to deposit: '))
        return amount
    except ValueError:
        print('Invalid amount.')
        return 0
    except Exception:
        print('Something went wrong...')
        return 0

# noinspection PyBroadException
def withdraw():
    try:
        amount = int(input('Enter amount to withdraw: '))
        return amount
    except ValueError:
        print('Invalid amount.')
        return 0
    except Exception:
        print('Something went wrong...')
        return 0
def save_balance(balance):
    with open('balance.json', 'w') as file:
        json.dump(balance, file)
def read_balance():
    try:
        with open('balance.json', 'r') as file:
            return json.load(file)
    except:
        return {}