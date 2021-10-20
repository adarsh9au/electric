# Name : Amritanshu Kumar Verma
# Roll No : 186301012
# Python Assignment 1
num = int(input())
ch = 'A'
for i in range(1,num+1):  
    str=""  
    for j in range(1,i+1):
        str = str+ch
    print(str)
    ch = chr(ord(ch) + 1)