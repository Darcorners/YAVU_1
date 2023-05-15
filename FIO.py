from datetime import datetime

print("Введите Имя: ")
Name = input()
print("Введите Фамилию: ")
SurName = input()
print("Введите Отчество: ")
LastName = input()
print("Введите Группу: ")
Group = input()
Year = 0
print("Введите Год Рождения: ")
GodR = int(input())
GodN = datetime.now()
Special = "Информационные системы"
FIO = Name + SurName + LastName

def Rod():
    Year = GodN.year - GodR
    print(f"Возраст: {Year}")


def Stud():
    print(f"Имя: {Name}, Фамилия: {SurName} , Отчество: {LastName} , Группа: {Group}")
    Rod()


class Student(object):
    def FILO(self):
        FIO = " ".join([Name, SurName, LastName])
        print(f"ФИО: {FIO}, Возраст: {Year}, Группа: {Group}, Специальность: {Special}")
