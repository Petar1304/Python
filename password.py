import random
import os

#generate password

def generate(site,username,n):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    signs = ['+','-','/','*','=','<','>','!','%','@','~','#','$','^','&']

    password = ''

    for i in range(n):
        number = str(numbers[random.randrange(0, len(numbers))])
        letter = letters[random.randrange(0, len(letters))]
        sign = signs[random.randrange(0, len(signs))]
        choise = [number, letter, sign]

        x = choise[random.randrange(0, len(choise))]
        password = password + x
    
    f = open('passwords.txt', 'a')
    f.write(site+ ': \n'+ '\tusername:'+ username+ '\n'+ '\tpassword: '+ password)
    f.write('\n')
    f.close()

    return password



print('-----------------------------')
site = input('Website: ')
username = input('username: ')
print('Number of characters: ')
n = int(input())
#print(generate(site,username,n))
print('Your password is generated, find it in file passwords!')
