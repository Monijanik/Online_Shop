import shop

shop_test = shop.Shop()

q1 = int(input('Enter as Admin or User? (1/2)'))
q2 = int(input('do you want to register or login? (1/2)'))


if q1 == 1:
    if q2 == 1:
        print('you are not allowed')
    elif q2 == 2:
        name = input('enter your name : ')
        password = input('enter the password:  ')
        res = shop_test.login_admin(name, password)  
        print(res)
elif q1 == 2:
    if q2 == 1:
        name = input('enter your name : ')
        password = input('enter the password: ')
        email = input('enter your email: ')
        birthdate = input('enter your birthdate: ')
        address = input('enter your address: ')
        res = shop_test.register_user(name, password, email, birthdate, address)
        print(res)
    elif q2 == '2':
        email = input('enter your email : ')
        password = input('enter the password: ')
        res = shop_test.login_user(email, password)
        print(res)
            
