import sys 
sys.stdin, sys.stdout = open('herding.in','r'), open('herding.out','w')
lst = list(map(int, input().strip().split()))
lst.sort()
l,h=0,0

if (lst[0]+1 == lst[1]) and (lst[1] + 1 == lst[2]):
    l = 0
elif (lst[0] + 2 == lst[1]) or (lst[1] + 2 == lst[2]):
    l = 1
else:
    l = 2

h = max([lst[1] - lst[0], lst[2] - lst[1]]) - 1
print(l)
print(h)
