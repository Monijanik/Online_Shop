import shop

shop_test = shop.Shop()

admin_is_loged_in = False
user_is_loged_in = False
q1 = input('Enter as Admin or User? (1/2)')
q2 = input('do you want to register or login? (1/2)')

while q1 != 'exit':
    if q1 == '1':
        if q2 == '1':
            print('you are not allowed')
        elif q2 == '2':
            name = input('enter your name : ')
            password = input('enter the password:  ')
            ok, res = shop_test.login_admin(name, password)  
            print(res)
            if ok:
                admin_is_loged_in = True
    elif q1 == '2':
        if q2 == '1':
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

while admin_is_loged_in:
    q1 = int(input('do you want to add a category or a product or see user list?(1/2/3) '))
    if q1 == 1:
        cat_name = input('please enter category name: ')
        shop_test.add_category(name)

            
