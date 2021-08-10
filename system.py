import os

# database:
data = {
    'user1': {
        'name': 'Petar',
        'money': 1234,
    },
    'user2': {
        'name': 'Nikola',
        'money': 1234,
    }
}



def GET():
    for item in data.keys():
        print('{} {}'.format(data[item]['name'], data[item]['money']))

def DELETE():
    pass

def POST():
    pass

def END():
    print('Turning off server...')
    exit()

if __name__ == '__main__':
    while True:
        print('Select type of operation:\n\t1) List all\n\t2) Add new\n\t3) delete\n\t4) end\n')
        option = input('Request: ')
        if option == '1':
            GET()
        elif option == '2':
            POST()
        elif option == '3':
            DELETE()
        elif option == '4':
            END()
        else:
            print('wrong code...\n')

        # os.system('cls')
