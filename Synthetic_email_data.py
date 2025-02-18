import random
from random import randint
import string

def random_emails(amount):
    emails = ['Email', 'duplicate1@gmail.com', 'DUPLICATE2@gmail.com']
    for username in range(amount):
        username = []
        domain = random.choice(['@gmail.com', '@outlook.com', '@company.eu', '@protonmail.io', '@yahoo.com', '@cloud.com'])
        username.append(string.digits[randint(1,9)] 
            + string.digits[randint(1,9)] 
            + string.ascii_letters[randint(1,29)] 
            + string.ascii_letters[randint(1,29)]
            + string.ascii_letters[randint(1,29)] 
            + string.digits[randint(1,9)] 
            + string.ascii_letters[randint(1,29)]
            )
        email = ''.join(username) + ''.join(domain)
        emails.append(email)
    emails = '\n'.join(emails)
    return emails
#print(random_emails(100))

file = open('Baigiamasis_darbas/Email_list.csv', mode= 'w', encoding= 'utf-8')
file.writelines(random_emails(3000))

def random_emails(amount):
    emails = ['Email', 'duplicate1@gmail.com', 'duplicate2@gmail.com']
    for username in range(amount):
        username = []
        domain = random.choice(['@gmail.com', '@outlook.com', '@company.eu', '@protonmail.io', '@yahoo.com', '@cloud.com'])
        username.append(string.digits[randint(1,9)] 
            + string.digits[randint(1,9)] 
            + string.ascii_letters[randint(1,29)] 
            + string.ascii_letters[randint(1,29)]
            + string.ascii_letters[randint(1,29)] 
            + string.digits[randint(1,9)] 
            + string.ascii_letters[randint(1,29)]
            )
        email = ''.join(username) + ''.join(domain)
        emails.append(email)
    emails = '\n'.join(emails)
    return emails
#print(random_emails(100))

file = open('Baigiamasis_darbas/Email_list_control.csv', mode= 'w', encoding= 'utf-8')
file.writelines(random_emails(3000))

file.close()
