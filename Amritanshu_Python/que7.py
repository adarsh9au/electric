# Name : Amritanshu Kumar Verma
# Roll No : 186301012
# Python Assignment 1
num = int(input())
ans = 1
for i in range(0,num):
    for j in range(1,(2**i)+1):
        print(ans,end="")
        ans = ans+1
        if ans==10:
            ans = 1
    print('\n',end = "")