from random_password_generator import password_generator as pg

print('u: upper, l: lower, d: digits, s: Symbols, ul: upper-lower, lds: lower-digits-symbols')
character = input('Enter the password type: ')
length = input('Length of password: ')

password = pg.PasswordGenerator(character, length)
password.set_charset()
password.generate_password()