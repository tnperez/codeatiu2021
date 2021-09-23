# ello 
# 4/2 = 2



def pal(s):
    l = len(s)
    l = l//2 # 7//2 = 3 or 7%2 = 1
    # firstHalf = ""
    # secHalf = ""
    # #for loops here
    # return firstHalf == secHalf
    for i in range(l):
        if(s[i] != s[len(s) - i - 1]):
            return False
    return True

def pal1(s):
    l = len(s) #elle -> 4
    l = l//2 #-> 2
    firstHalf = ""
    secHalf = ""

    for i in range(l): #0,1
        firstHalf += s[i]
    if(len(s)%2 == 1):
        for j in range(len(s) - 1, l , -1): #(3,2,-1) #- (1 - len(s)%2)
            secHalf += s[j]
    else:
        for j in range(len(s) - 1, l - 1 , -1): #(3,2,-1) #- (1 - len(s)%2)
            secHalf += s[j]
    
    return firstHalf == secHalf

i = input("Enter a word: ")
print("Your word came back as ", pal1(i), " for the check")
while(i != "QUIT"):
    i = input("Enter a word: ")
    print("Your word came back as ", pal1(i), " for the check")