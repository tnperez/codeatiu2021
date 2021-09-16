import math
x = 2
y = 3
# + - / % // ** * 
def add(param1,param2):
    return param1 + param2

print(add(x,y))

if x == y:
    print("They are the same!")
elif x > y:
    print("X is bigger it is: ",x)
else: 
    print("Y is bigger it is: ",y)

lst = [1,2,3,4,5,6]
counter = 0
print("----------------While----------------")
while(counter < len(lst)):
    print("lst[",counter,"]: ", lst[counter])
    counter += 1 #counter = counter + 1
print("----------------For range----------------")
for i in range(0,len(lst)):
    print("lst[",i,"]: ", lst[i])
print("----------------For lst-----------------")
for i in lst:
    print(i)

print("----------------Recursion-----------------")
def lstPrint(lst):
    if(len(lst) < 1):
        return 0
    else:
        print(lst[0])
        lstPrint(lst[1:])

lstPrint(lst)

s1 = "hello"
s2 = "racecar"

def palindrome(s):
    #solution here
    return True or False