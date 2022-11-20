import time
count = 0
while count == 0:
    vybor = input("пожалуйста введите что вы хотите register или log in: ").lower()
    aut = 'register'
    login = 'log in'
    logins = ['Kesha', "Gesha"]
    passwords = ['keshakrasava', "12345678"]
    da = 'yes'
    net = 'no'
    vosstanovka = '123456'
    ex = 'exit'
    if vybor == aut:
        login = input('Создайте свой логин: ')
        if login in logins:
            from random import *
            o = (''.join([choice('''1234567890qwertyuiop''') for x in range(6)]))
            print('Такой логин уже существует. Можете создать новый или выбрать один из вариантов: ', login + '.' + o[0: 2], ', ', login + '_' + o[2:4],', ', login.upper() + '__' + o[4:6] )
            while login in logins:
                login = input('Введите новый логин: ')
        password = input('Создайте свой пароль: ')
        s = len(password)
        if s < 8:
            while s < 8:
                password = input('Пароль должен содержать не меньше 8ми символов, Введите новый пароль: ')
                u = len(password)
                s = u
            logins.append(login)
            passwords.append(password)
            print('Добро пожаловать ', login, ',ваш пароль', password)
            print(logins)
            print(passwords)
            count += 1
        else:
            logins.append(login)
            passwords.append(password)
            print('Добро пожаловать', login, ' Ваш пароль ', password)
            print(logins)
            print(passwords)
            count += 1
    elif vybor == login:
        login1 = input('Введите свой логин: ')
        if login1 in logins:
            password1 = input('Введите свой пароль: ')
            if password1 in passwords:
                while password1 != passwords[logins.index(login1)]:
                    password1 = input("Неправильный пароль повторите попытку. ")
                print('Добро пожаловать!')
                print(logins)
                print(passwords)
                count += 1
            else:
                print('Неверный пароль. Забыли пароль?')
                a = input().lower()
                if a in da:
                    time.sleep(3)
                    print("Уведомление ! Ваш код : 123456 ")
                    time.sleep(2)
                    kod = input('Введите шести значный код: ')
                    if kod in vosstanovka:
                        b = input('Введите новый пароль: ')
                        n = len(b)
                        if n < 8:
                            while n < 8:
                                b = input('Новый пароль должен содержать как минимум 8 символов, Введите новый пароль: ')
                                q = len(b)
                                n = q
                            print('Пароль успешно восстановлен, Теперь ваш пароль: ', b)
                            passwords[logins.index(login1)] = b
                            print(logins)
                            print(passwords)
                            count += 1
                        else:
                            print('Пароль успешно восстановлен, Теперь ваш пароль: ', b)
                            passwords[logins.index(login1)] = b
                            print(logins)
                            print(passwords)
                            count += 1
                    else:
                        while kod not in vosstanovka:
                            v = input("Код не правильный, повторите попытку: ")
                            if v in ex:
                                break
                            kod = v
                            if v in vosstanovka:
                                d = input('Введите новый пароль: ')
                                while len(d) < 8:
                                    d = input("Новый пароль должен содержать не меньше 8ми символов: ")
                                print('Пароль успешно всстановлен, теперь ваш пароль: ', d)
                                passwords[logins.index(login1)] = d
                                print(logins)
                                print(passwords)
                                count += 1
                elif a in net:
                    print('Ок')
        else:
            print('Такой аккаунт не найден')
    else:
        print('Ошибочка вышла')