grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# преобразуем список оценок в список средних баллов учеников в алфавитном порядке
grades_1 = []
grades_1.append(sum(grades[0])/len(grades[0]))
grades_1.append(sum(grades[1])/len(grades[1]))
grades_1.append(sum(grades[2])/len(grades[2]))
grades_1.append(sum(grades[3])/len(grades[3]))
grades_1.append(sum(grades[4])/len(grades[4]))
print(grades_1)

# преобразуем множество учеников в список учеников в алфавитном порядке
students_1 = sorted(list(students))
print(students_1)

# поместим данные в словарь
grades_of_students = {}
for y in range(len(students_1)):
    grades_of_students[students_1[y]] = grades_1[y]
print(grades_of_students)

# или с округлением балов до десятых
grades_of_students_1 = {}
for y in range(len(students_1)):
    grades_of_students_1[students_1[y]] = round(grades_1[y],1)
print(grades_of_students_1)