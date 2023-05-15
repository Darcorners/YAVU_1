import Workers as W

print("Введите Должность: ")
Dolz = input()
print("Введите Оклад: ")
Oclad = int(input())
POclad = ()
print("У вас есть автомобиль (0 , 1): ")
Car = int(input())
print("\n")
prime = ()
x = W.worker

def Work():
    if Dolz in x:
        if Dolz == 'Администратор':
            prime = W.prime[2]
            print(f"Ваш процент премии: {prime}%")
            POclad = Oclad + (Oclad * prime / 100)
            print(f"Ваш оклад с премией: {POclad}")
        elif Dolz == 'Директор':
            prime = W.prime[2]
            print(f"Ваш процент премии: {prime}%")
            POclad = Oclad + (Oclad * prime / 100)
            print(f"Ваш оклад с премией: {POclad}")
        elif Dolz == 'Менеджер':
            prime = W.prime[1]
            print(f"Ваш процент премии: {prime}%")
            POclad = Oclad + (Oclad * prime / 100)
            print(f"Ваш оклад с премией: {POclad}")
        elif Dolz == 'Охранник':
            prime = W.prime[0]
            print(f"Ваш процент премии: {prime}%")
            POclad = Oclad + (Oclad * prime / 100)
            print(f"Ваш оклад с премией: {POclad}")
    else:
        print("Данная должность не существует")

def car():
    if Car == 1:
        print('Вам проездной не нужен т.к. у вас есть авто')
    else:
        print('Вам положен проездной')
    W.auto += 1
    print(W.auto)

Work()
car()