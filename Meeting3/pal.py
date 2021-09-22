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


i = input("Enter a word: ")
print("Your word came back as ", pal(i), " for the check")
while(i != "QUIT"):
    i = input("Enter a word: ")
    print("Your word came back as ", pal(i), " for the check")