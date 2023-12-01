# n,m,k = map(int, input().split())
# nums = list(map(int, input().split()))

n,m,k = 5,8,3
nums = [2,4,5,4,6]

# 내림차순 정렬
nums.sort(reverse=True)

# 가장 큰 숫자
first = nums[0]

# 두번 째로 큰 숫자
second = nums[1]

# 결과
result = 0


count = ((m // (k + 1)) * k) + (m % (k+1))

result += count * first
result += (m - count) * second

print(result)
