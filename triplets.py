inp11=int(input())
List1=list(map(int,input().split()))
temp=0
for i in range(len(List1)-2):
    for j in range(i+1,len(List1)-1):
        for k in range(j+1,len(List1)):
            if List1[i]<List1[j]<List1[k] and i<j<k:
                temp=temp+1
print(temp)
