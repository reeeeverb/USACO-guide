import sys

sys.stdin, sys.stdout = open('sleepy.in', 'r'), open('sleepy.out', 'w')

n = int(input())
in_list = list(map(int,input().split()))
ans = 0

for i in range(n-1,0,-1):
    if in_list[i] < in_list[i-1]:
        ans = i
        break
print(ans)
