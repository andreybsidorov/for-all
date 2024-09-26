import random

students = ["Аполлон","Ярослав","Александра","Дарья","Ангелина"]
students.sort()
classes = ["Математика","Информатика","Русский язык"]
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')

print('''Список команд:
1. Добавить оценки ученика по предмету
2. Удалить оценки ученика по предмету
3. Вывести все оценки одного ученика
4. Вывести средний балл каждого предмета определённого ученика
5. Вывести все оценки по всем ученикам
6. Вывести средний балл по всем предметам по каждому ученику
7. Добавление предмета
8. Удаление предмета
9. Добавление ученика
10. Удаление ученика
11. Выход из программы 
''')
while True:
    command = int(input("Введите команду:"))
    if command ==1:
        print("1. Добавить оценку ученика по предмету: ")
        student = input("Введите имя ученика: ")
        class_ = input("Введите предмет: ")
        mark = int(input("Введите оценку: "))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f"Для {student} по предмету {class_} добавлена оценка {mark}")
        else:
            print("ОШИБКА: неверное имя ученика или название предмета")

    elif command == 2:
        print("2. Удалить оценку ученика по предмету ")
        print(students)
        student = input("Введите имя ученика: ")
        if student in students_marks.keys():
            print(student)
            for class_, marks in students_marks[student].items():
                print(class_, marks)
        else:
            print("ОШИБКА: Неправильно введено имя ученика")
            break
        class_ = input("Введите предмет: ")
        mark = int(input("Введите оценку: "))
        if class_ in students_marks[student].keys() and mark in students_marks[student][class_]:
            students_marks[student][class_].remove(mark)
            print(f"Для {student} по предмету {class_} удалена оценка {mark}")
            for class_, marks in students_marks[student].items():
                print(class_, marks)
        else:
            print("ОШИБКА: Неправильно введены предмет или оценка ")

    elif command == 3:
        print("3. Вывести все оценки одного ученика:  ")
        print(students)
        student = input("Введите имя ученика: ")
        if student in students_marks.keys():
            print(student)
            for class_, marks in students_marks[student].items():
                print(class_, marks)
        else:
            print("ОШИБКА: неверное имя ученика")

    elif command == 4:
        print("4. Вывести средний балл каждого предмета определённого ученика")
        print(students)
        student = input("Введите имя ученика: ")
        if student in students_marks.keys():
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f"\t{class_} - {marks_sum // marks_count}")
        else:
            print("ОШИБКА: неверное имя ученика ")

    elif command == 5:
        print("5. Вывести все оценки по всем ученикам ")
        for student in students:
            print(student)
            for class_ in classes:
                print(f"\t{class_} - {students_marks[student][class_]}")

    elif command == 6:
        print("6. Вывести средний балл по всем предметам по каждому ученику ")
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f"\t{class_} - {marks_sum // marks_count}")

    elif command == 7:
        print("7. Добавление предмета ")
        print(classes)
        new_class_ = input("Введите предмет: ")
        if new_class_ not in students_marks[student].keys():
            classes.append(new_class_)
            for student in students_marks:
                students_marks[student][new_class_] = []
            print(classes)
            print(students_marks[student].keys())
        else:
            print("Предмет уже есть в списке ")

    elif command == 8:
        print("8. Удаление предмета ")
        print(classes)
        class_ = input("Введите название предмета: ")
        if class_ in classes:
            classes.remove(class_)
            del students_marks[student][class_]
            print("Предмет удалён ")
            print(classes)
            print(students_marks[student])
        else:
            print("Предмета нет в списке ")

    elif command == 9:
        print("9. Добавление ученика ")
        print(students)
        new_student = input("Введите имя ученика: ")
        if new_student not in students_marks.keys():
            students.append(new_student)
            students_marks[new_student] = {}
            print(students)
            print(students_marks)
        else:
            print("Данный ученик уже есть в списке ")

    elif command == 10:
        print("10. Удаление ученика: ")
        print(students)
        student = input("Введите имя: ")
        if student in students_marks.keys():
            students.remove(student)
            del students_marks[student]
            print(students)
            print(students_marks)
        else:
            print("Данного ученика нет в списке ")

    else:
        if command == 11:
            print("11. Выход из программы ")
    break