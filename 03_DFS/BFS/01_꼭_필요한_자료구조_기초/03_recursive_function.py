'''
재귀함수는 자기 자신을 다시 호출하는 함수이다. 보통 파이썬 인터프리터는 호출 횟수 제한이 있기에 무한히 재귀 호출을 진행할 수 없다.
그러므로 재귀 함수의 종료 조건을 꼭 명시해야한다.
'''

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

