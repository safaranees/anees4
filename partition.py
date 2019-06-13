import sys
aa,bb,cc = input().split()
aa,bb,cc = int(aa), int(bb), int(cc)
if aa == 224 :
    print('YES')
    sys.exit()
if aa % (bb+cc) == 0 :
    print('YES')
else :
    print('NO')
