import afzal
import account
afzal.line()
print('                          Welcome to AfzalBank! ')
afzal.line()

def main():
    global successful, username
    try:
        auth = int(input('1. Sign Up\n2. Log In\nEnter your choice: '))
        if auth == 1:
            account.sign_up()
            afzal.line()
            print('You should to Log In')
            successful, username = account.log_in()
        elif auth == 2:
            successful, username = account.log_in()

        if not successful:
            return
        balance = afzal.read_balance()

        if username not in balance:
            balance[username] = 0
        running = True
        while running:
            afzal.line()
            action = int(input('1. Deposit\n2. Withdraw\n3. View balance\n0. Exit\nEnter your choice: '))
            if action == 1:
                afzal.line()
                balance[username] += afzal.deposit()
                afzal.save_balance(balance)
                print(f'Your balance is ${balance[username]}')
            elif action == 2:
                afzal.line()
                amount = afzal.withdraw()
                if amount > balance[username]:
                    print('Not enough money!')
                else:
                    balance[username] -= amount
                    afzal.save_balance(balance)
                    print(f'Your balance is ${balance[username]}')
            elif action == 3:
                afzal.line()
                print(f'Your balance is ${balance[username]}')
            elif action == 0:
                afzal.line()
                print(f'Thank you for using AfzalBank!\n See you next time {balance[username]}!')
                afzal.line()
                running = False
    except Exception:
        print('Something went wrong...')
main()


