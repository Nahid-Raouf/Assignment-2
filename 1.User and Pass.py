username = 'NAHID'
password = '1379'

i = 0 

while (i < 3) :
    
    username_entered = input('Enter username:')
    password_entered = input('Enter password :')

    if (username == username_entered) & (password == password_entered) :
        print('Login was successful...')
        break
    else :
        i = i+1
        print('Login was failed!')
        
        
if 3 <= i :
    print('You locked , Please try again later....')