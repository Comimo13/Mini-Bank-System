import json
db_username = []
db_password = []
def save_account():
    with open('accounts.json', 'w') as file:
        json.dump(db_accaunt, file)
def save_password():
    with open('passwords.json', 'w') as file:
        json.dump(db_password, file)
def save_username():
    with open('usernames.json', 'w') as file:
        json.dump(db_username, file)
def read_account():
    global db_accaunt
    with open('accounts.json', 'r') as file:
        db_accaunt = json.load(file)
        return db_accaunt
def read_password():
    global db_password
    with open('passwords.json', 'r') as file:
        db_password = json.load(file)
        return db_password
def read_username():
    global db_username
    with open('usernames.json', 'r') as file:
        db_username = json.load(file)
        return db_username


db_accaunt = dict(zip(db_username , db_password))
save_account()

signed = None
def log_in():
    try:
        global signed
        username = input('Enter username: ')
        password = input('Enter password: ')
        if username in read_username() and password in read_password():
            print(f'Login successful\nWelcome back {username.capitalize()}!')
            signed = True
            return True , username
        else:
            print('Invalid username or password')
            signed = False

    except ValueError:
        print('Invalid username or password')
    except Exception:
        print('Something went wrong...')


def sign_up():
    try:
        username2 = input('Enter new username: ')
        password2 = input('Enter new password: ')
        db_password.append(password2)
        db_username.append(username2)
        save_username()
        save_password()
        print('You have been signed up.')
    except KeyError:
        print('Invalid username or password')
    except TypeError:
        print('Invalid username or password')
    except ValueError:
        print('Invalid username or password')


