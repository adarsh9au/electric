# Name : Amritanshu Kumar Verma
# Roll No : 186301012
# Python Assignment 1
num = int(input())
temp = 0
i = 1
while temp<num:
    val = (3*i)+2
    if val%4!=0:
        temp = temp+1
        print(val,end=" ")
    i = i+1
