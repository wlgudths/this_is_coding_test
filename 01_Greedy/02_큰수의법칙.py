n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

# 내림차순 정렬
nums.sort(reverse=True)

# 가장 큰 숫자
first = nums[0]

# 두번 째로 큰 숫자
second = nums[1]

# 결과
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break

    result += second
    m -= 1

print(result)