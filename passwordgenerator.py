#!/usr/bin/python3
import random

def randomize(total = 30):
    """Returns string of random chars"""
    retstr = ''
    datei = open('../Sonstiges/charsallowed.txt','r')
    i = 0
    allowed = datei.read()
    while i <= total and len(retstr) <= 20:
        r = chr(random.randint(33,122))
        if r in allowed:
            retstr += r
        i += 1
    
    datei.close
    return retstr


website = input('Enter name of Website here:  ')
usrnm = input('Enter UserName here:  ')
email = input('Enter User Email here:  ')
file = open('../Sonstiges/Login_information.txt', 'a')
pwd = randomize()

file.write('Website: ')
file.write(website)
file.write('\n')
file.write('UserName: ')
file.write(usrnm)
file.write('\n')
file.write('Email: ')
file.write(email)
file.write('\n')
file.write('Password: ')
file.write(pwd)
file.write('\n')
file.write('\n')
file.close

