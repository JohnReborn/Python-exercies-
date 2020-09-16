# Exercise 7
#given the list variable, take the list that only has even elements of this list

a = [1,4,9,16,25,36,49,64,81,100]
newlist = []

for x in a:
    if x % 2 ==0:
        newlist.append(x)

print(newlist)
