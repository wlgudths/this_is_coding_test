# 3-1. 거스름돈

# 입력 받기
n = int(input())

# 거스름돈
coins = [500, 100, 50, 10]

# 카운트
cnt = 0

for coin in coins:
    cnt += n // coin
    n %= coin


print(cnt)