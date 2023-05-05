def z_1():
    n=int(input("Введите количество слов "))
    c=""
    for i in range (n):
        a=input ("Введите слово ")
        c=c+" " +a
    print(c)
def z_2():
    c = ""
    a = input("Введите слово ")
    while a!="stop":
        a = input("Введите слово ")
        c = c + " " + a
    print(c)
def z_3():
    a = input("Введите слово ")
    if "ф" in a:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
def z_4():
    import random

    n=0
    p=0
    while n!=3:
        a = int(random.uniform(1, 10))
        b = int(random.uniform(1, 10))
        sum = a + b
        v="Введите сумму "+str(a)+"+"+str(b) + "="
        m=int(input(v))
        if m==sum:
            p=p+1
            print("Правильно!")
        else:
            n=n+1
            print("Ответ неверный")
    print("Игра окончена. Правильных ответов: ", p)
z_1()
z_2()
z_3()
z_4()