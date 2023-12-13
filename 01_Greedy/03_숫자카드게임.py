n,m = map(int, input().split())

# 결과
result = 0

for i in range(n):
    data = list(map(int, input().split()))

    # 현재 행에서 가장 낮은 숫자
    min_value = min(data)

    # result 와 낮은 숫자를 비교하면 가장 큰 숫자 선택
    result = max(result, min_value)


print(result)
