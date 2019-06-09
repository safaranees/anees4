num=int(input())
str1=[]
for j in range(0,num):  
    num1=input()
    str1.append(num1)
x1=[]
for j in zip(*str1):
    if j.count(j[0])==len(j): 
        x1.append(j[0])
    else:
        break
print(''.join(x1))
