
N = int(input())
students = []
for _ in range(N):
    name = input()
    score = float(input())
    students.append([name, score])

# Сортировка списка по оценкам в порядке убывания
students.sort(key=lambda x: x[1], reverse=True)

# Получение списка оценок
scores = [student[1] for student in students]
# создание альтернативного списка без максимальной по величине оценки
ma=max(scores)
b= [x for x in scores if x != ma]

# Нахождение второй по величине оценки
second_max_score = b[0]

# Создание списка имен студентов со второй по величине оценкой
second_max_students = []
for student in students:
    if student[1] == second_max_score:
        second_max_students.append(student[0])

# Сортировка имен студентов в алфавитном порядке
second_max_students.sort()

# Вывод имен студентов со второй по величине оценкой
for student in second_max_students:
    print(student)