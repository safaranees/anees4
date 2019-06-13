str1,str2=input().split()
t=abs(len(str1)-len(str2))
for i in range(len(str1)):
    if len(str2)==1 and str2[i] in str1:
        break
    if str1[i]!=str2[i]:
        t+=1
print(t)
