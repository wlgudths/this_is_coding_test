# n 팩토리얼 구현

# 반복문
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i

    return result

# 재귀 함수
def factorial_iterative_r(n):
    if n <= 1:
        return 1
    return n * factorial_iterative_r(n - 1)


print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_iterative_r(5))