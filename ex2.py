# Exercise 2
#Ask the user for a number, Depending on whether the number is even or odd
#print appropriate message to the user

#First ask user for a number
num int(input("Enter a Number to check\n") 
check = int(input("Give a number to divide by:\n")
    

if num % 4 == 0:
        print(num, "is a multiple of 4")

elif num % 2 ==0:
    print(num,"is even")

else:
    print(num, " is odd")


if num % check == 0:
    print(num, "divides evenly by", check)

else:
    print(num, "does not divide evenly by", check)
    
        
