from itertools import combinations
string11,n2=map(int,input().split())
n3=len(str(string11))
a11=list(combinations(str(string1),n3-n2))
a11=(sorted(a11))
b11="".join(a11[0])
print(b11)
