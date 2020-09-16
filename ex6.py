# Exercise 6
#Ask user for a string that prints out whether this string is a palindrome or not
# meaning string that reads the same forwards and backwards
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
