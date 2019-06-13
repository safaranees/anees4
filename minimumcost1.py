str1,str2=input().split()
tempp=0
if len(str1)>len(str2):
  str1,str2=str2,str1
i=0
while i<len(str1):
  tempp+=(ord(str2[i])-ord(str1[i]))
  i+=1
for i in range(i,len(str2)):
  tempp+=ord(str2[i])-ord('a')+1
print(tempp)
