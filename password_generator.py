import re
import string
import random

class PasswordGenerator:
    #---charset: u,l,U,L,d,D,s,S
    #--- length : length of password.
    def __init__(self, charset, length):
        self.charset = charset
        self.length = int(length)
        self.charset_arr = []
        self.password = []

#---user: ulD

    def set_charset(self):
        if re.search('u',self.charset) or re.search('U',self.charset):
            self.charset_arr.append(string.ascii_uppercase)
        if re.search('l',self.charset) or re.search('L',self.charset):
            self.charset_arr.append(string.ascii_lowercase)
        if re.search('d',self.charset) or re.search('D',self.charset):
            self.charset_arr.append(string.digits)
        if re.search('s',self.charset) or re.search('S',self.charset):
            self.charset_arr.append(string.punctuation)

    # CharsetArr : ['ABC....Z', 'abc...z','0123...']
    # length : 5
    # 1: 3i5Wa

    def generate_password(self):
        if len(self.charset_arr) == 0:
            return
        for i in range(self.length):
            word = self.charset_arr[random.randrange(len(self.charset_arr))] # abc...z = 26
            self.password.append(word[random.randrange(len(word))]) # t
        print('Random generated password is: {}'.format(''.join(self.password)))