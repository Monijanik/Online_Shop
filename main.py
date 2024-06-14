import shop

shop = shop.Shop()

q1 = input('Enter as Admin or User? (1/2)')
q2 = input('do you want to register or login? (1/2)')

while q1.isdigit() and q2.isdigit():
    if q1 == 1:
        if q2 == 1:
            print('you are not allowed')
        elif q2 == 2:
            name = input('enter your name : ')
            password = input('enter the password:  ')
            shop.login_admin(name, password)  
    elif q1 == 2:
        if q2 == 1:
            name = input('enter your name : ')
            password = input('enter the password: ')
            email = input('enter your email: ')
            birthdate = input('enter your birthdate: ')
            address = input('enter your address: ')
            shop.register_user(name, password, email, birthdate, address)
        elif q2 == '2':
            email = input('enter your email : ')
            password = input('enter the password: ')

            
