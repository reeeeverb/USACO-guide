import sys

sys.stdin, sys.stdout = open('milkorder.in', 'r'), open('milkorder.out', 'w')

n,m,k = map(int,input().split())

heir = list(map(int,input().split()))
req = []
order = [0]*(n)
for i in range(k):
    temp = list(map(int,input().split()))
    order[temp[1]-1] = temp[0]
    if temp[0] in heir:
        pos = heir.index(temp[0])
        o = 1
        for c in heir[:pos][::-1]:
            while True:
                if order[temp[1]-o] == 0:
                    order[temp[1]-o] = c
                    o+=1
                    break
                else:
                    o+=1

print(order.index(0)+1)


