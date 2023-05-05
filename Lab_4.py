def z_1(ch: int):
    if ch%3==0:
        return True
    else:
        return False

def z_2(ch):
    it=None
    try:
        it=100/ch
    except ValueError:
        print("Введите число")
    except ZeroDivisionError:
        print("Делить на 0 нельзя")
    except Exception as o:
        print("Ошибка:", o)
    return it
def z_3(d: str):
    d=d.split(".")
    try:
        if int(d[0])*int(d[1])==int(d[2][2:]):
            return True
        else:
            return False
    except:
        print("Дата должна быть в формате дд.мм.гггг")
def z_4(n: str):
    if len(n)%2!=0:
        return "Количество цифр должно быть чётным"
    else:
        s1=0
        s2=0
        for i in range (len(n)//2):
            s1+=int(n[i])
            s2+=int(n[len(n)-1-i])
        if s1==s2:
            return True
        else:
            return False
k=6
print("Проверка числа", k, "на делимость на 3")
print((z_1(k)))
k=38
print("Проверка числа", k, "на делимость на 3")
print((z_1(k)))

print("\n")
k=10
print("Проверка делимости 100 на число", k)
print((z_2(k)))
k=7
print("Проверка делимости 100 на число", k)
print((z_2(k)))

print("\n")
k="11.05.2004"
print("Проверка даты",k ,"на магическое значение")
print(z_3(k))
k="02.11.2022"
print("Проверка даты",k ,"на магическое значение")
print(z_3(k))

print("\n")
k="560480717"
print("Проверка счастливого номера билета", k)
print(z_4(k))
k="190820"
print("Проверка счастливого номера билета", k)
print(z_4(k))