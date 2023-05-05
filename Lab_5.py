def z_1(n):
    n=int(input("Введите число: "))
    m=[2,4,5,3,7]
    if n in m:
        s=str(m)+"\n"+str(n)+"\n Поздравляю, Вы угадали число!"
    else:
        s=str(m) + "\n" + str(n) + "\n Нет такого числа"
    return s
def z_2(n):
    m=[]
    for i in range (len(n)-1):
        if n[i] in n[i+1:]:
            m.append(n[i])
    set(m)
    return m
def z_3(n):
    if n>7:
        return "Дней в неделе 7"
    else:
        d=("Понедельник", "Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
        m=list(d)
        v=m[7-n:7]
        r=m[0:7-n]
        s="Ваши выходные дни:"+str(v)+"\n Ваши рабочие дни:"+str(r)
        return s
def z_4(n):
    import random
    c1=["Серов", "Пушин", "Винина","Ефлютина","Сидоров"]
    c2=["Смирнов","Минина", "Яковлева","Носов", "Иванов"]
    sk=[]
    sk.append(c1[int(random.uniform(0, len(c1)))])
    sk.append(c2[int(random.uniform(0, len(c2)))])
    sk=tuple(sk)
    print("Список 1:",c1,"\n Список 2:", c2)
    print("Спортивная команда:", sk)
    print("Количество участников спрот команды:",len(sk))
    sk2=tuple(sorted(sk))
    print("Отсортированный список спорт. команды:",sk2)
    k=sk.count("Иванов")
    return ("Кол-во повторений фамилии Иванов", k)

print(z_1(4))

n=[2,4,6,2,4,3,5]
print("Повторяющиеся значения в списке",n,z_2(n))

n=int(input("Cколько выходных вы хотите?"))
print(z_3(n))

print(z_4(1))