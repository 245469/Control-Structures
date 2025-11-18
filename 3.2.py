###
# Checking login and password
#
login = 'Naruto'
password = 'Sakura'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password :
    print(f'You are logged in')
else:
    print(f'Incorrect login or password!!')