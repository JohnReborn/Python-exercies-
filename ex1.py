# Exercise 1
# Create a program that asks user to enter their name and age
#print message addressed to them that tell them the year they will turn 100

name = input("Please enter your name\n")
age  = int(input("What is your age?\n"))

years = str((2020 - age) +100)

print(name, "Your age is ", age, "and you will be 100 in ", years)
