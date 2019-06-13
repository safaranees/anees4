ri=int(input())
si=list(map(int,input().split()))
ct=0
for i in range(len(si)-2):
    for x in range(i+1,len(si)-1):
         for j in range(x+1,len(si)):
            if si[i]<si[x]<si[j] and i<x<j:
                ct+=1
print(ct)
