n,k = map(int, input().split())

cnt = 0

# n이 1이 될 때까지
while n != 1:
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)
