name_list=[]
score_list=[]
grade_list=[]
print('How many students?')

for _ in range(int(input())):
    print('Write the student name')
    name = input()
    name_list.append(name)
    print('Write the grade')
    score = float(input())
    score_list.append(score)
    grade = (name, score)
    grade_list.append(grade)

print(grade_list)
