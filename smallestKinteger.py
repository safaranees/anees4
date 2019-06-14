from itertools import combinations
string1,num1=map(int,input().split())
n1=len(str(string1))
L1=list(combinations(str(string1),n1-num1))
L1=(sorted(L1))
b1="".join(L1[0])
print(b1)
