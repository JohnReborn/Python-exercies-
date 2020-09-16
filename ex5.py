# Exercise 5
# Write a program that returns a list that contains only the elements that are common
#between the lists( no duplicates)

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
total = (a+b)

newList = []
for x in total:
    if total.count(x)==1:
        newList.append(x)

print(newList)
