# Get 20 random marks for 20 students (between 0 to 100). Create 3 separate lists . The first list should contain the marks <=30. The second list is between 31 to 69. The third list >= 70.
# Display the output lists.
import random


marks_students[]
for marks in range ( 20 ):
    score = random.randint(0,100)
    marks_students.append(score)

print(marks_students)

list1 = []
list2 = []
list3 = []

for marks in marks_students:
    if (marks <= 30):
        list1.append(marks)
    elif (marks >= 31 or marks <=69):
        list2.append(marks)
    else :
        list3.append(marks)


print("list1" , list1)

print("list2" , list2)

print("list3" , list3)



