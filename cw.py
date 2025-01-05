#list is for mstoring same or different kind of data

fruits = ["apple" , "banana" , "cherry" , "pineapple"]
#print(fruits)

#indexing is accessing elements
#print(fruits(3))


# negati8ve index
#print(fruits(-1)) 

#add an element
#append()
fruits.append("mango")

fruits.append("orange")
print(fruits(5))

#remove a function
#remove
fruits.remove("banana")

#slicingh
fruits2 = fruits[0:3]
print(fruits2)

print("=================2D list ============")

#create a 2D list
list2d = [[1,2,3] , [3,4,5],  [5,6,7]]

print(list2d[0][1])

print(list2d[1][2])

#length of the fruits list is 5

#length of 2d list is 3
#length of smaller list is 3

#len(list2d)
print("length of 2d :" , len(list2d))

print(len(list2d[0]))

#literating through every element in the list
for row in range(len(list2d)):
    for element_in_row in range(len(list2d[0])):
        print(list2d(row)(element_in_row) , end= " "
    print()"\n")


