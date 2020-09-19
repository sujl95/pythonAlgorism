n, k = map(int,input().split())

result = 0

cnt = 0
ck = True
while(ck):
    if n % k == 0:
        n /= k
    else:
        n -= 1
    if n == 1:
        ck = False
    cnt += 1


print(cnt)