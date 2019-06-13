import math
inp1=int(input())
string1=math.log10(inp1)/math.log10(2)
if math.ceil(string1)==math.floor(string1):
	print("0")
else:
    c=(inp1-1)//2
    string1=c*2
    print(inp1-string1)
