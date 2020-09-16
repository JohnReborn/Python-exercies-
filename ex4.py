# Exercise 4
# Create a program that asks user for a number then prints out a list
#of all divisors of that number(number with no reminder)

num = int(input("Please choose a number to divide\n"))

listRange = list(range(1, num+1))

divisorList = []

for x in listRange:
    if num % x == 0:
        divisorList.append(x)

print(divisorList)
