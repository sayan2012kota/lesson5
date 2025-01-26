from random import randint


age_people = []

for age in range ( 20 ):
    age2 = randint(0,100)
    age_people.append(age2)

print(age_people)

list1 = []
list2 = []
list3 = []

for age in age_people:
    if (age < 18):
        list1.append(age)
    elif (age >= 18 and age <=50):
        list2.append(age)
    else :
        list3.append(age)


print("list1" , list1)

print("list2" , list2)

print("list3" , list3)



