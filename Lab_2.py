def z_1():
    p=input("Введите пароль:")
    if len(p)<5:
        print("Короткий пароль")
    elif p[0:6]=="11111":
        print("Ненадежный пароль")
    else: print(p)
    b=False
    for char in p:
        if char.isnumeric()==False:
            b = True
    if b==False:
            print("Добавьте буквы ")
    p2=input("Повторите пароль: ")
    if p==p2:
        print(p)
    else:
        print("Неверно введен пароль ")
def z_2 ():
    a = int(input("Введите номер места:"))
    if a > 36 and a < 55:
            print("Ваше место боковое")  
    elif a < 37:
        if a % 2 == 1:
            print("Ваше место нижнее купе")
        else:
            print("Ваше место верхнее купе ")
    else:
        print("Места не существует")
def z_3 ():
    a=int(input ("Введите год"))
    if a%4 ==0 and a%100!=0 or a%400==0:
        print("Год", a, "високосный")
    else:
        print("Год", a, "не високосный")
def z_4():
    c = ("красный", "синий", "жёлтый")
    a = input("Введите цвет:")
    b = input("Введите цвет:")
    if a in c and b in c:
        if (a == "красный" and b == "жёлтый") or (a == "жёлтый" and b == "красный"):
            print(a, "+", b, "= оранжевый")
        if (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
            print(a, "+", b, "= фиолетовый")
        if (a == "жёлтый" and b == "синий") or (a == "синий" and b == "жёлтый"):
            print(a, "+", b, "= зелёный")
    else:
        print("Цветов нет в базе данных")
z_1()
z_2()
z_3()
z_4()