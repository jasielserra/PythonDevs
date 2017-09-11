'''
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print
each name on a new line.

By HackerRank

'''


students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
        
students.sort(key=lambda x: x[1])
second_lowest_grade = students[0][1]
    
for name,grade in students:
    if grade > second_lowest_grade:
        second_lowest_grade = grade
        break

names = []     

for name, grade in sorted(students):
    if grade == second_lowest_grade:
        names.append(name)

print('\n'.join(names)) 
