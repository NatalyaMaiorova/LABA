a=input("Введите пароль: ")
b=input("Повторите пароль: ")
if a==b:
    if len(a)<8 or len(b)<8:
        print("Ненадежный пароль")
    else:
        print("Пароль принят")
else:
    print("Пароли не совпадают")
