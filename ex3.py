# Exercise 3
# Write a program that prints all elements of the list that are less than 5
#Make a new list that has all elements less than 5 from this list and print
#Ask user for number and return a list that contains only elements from the original list 'a'
#that are smaller than the number given by user

a = [1,1,2,3,5,8,13,21,34,55,89]

for x in a:
    if x < 5:
        print(x)

newList = []
for x in a:
    if x <5:
        newList.append(x)
        print(x)


num = int(input("Enter a number\n"))

for x in a:
    if x< num:
        print(x)
