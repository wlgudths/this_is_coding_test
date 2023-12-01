# 입력
n = int(input())

# 방향 계획서
plans = input().split()

# 방향 딕셔너리
dict_plan = {'R':0, 'L':1, 'D':2, 'U':3}

# 인덱스 방향
idx = []

# N X N 지도
map = [[0] * n for _ in range(n)]

# 방향 R L D U
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 시작 위치
x,y = 0,0

# 방향 인덱스 담기
for plan in plans:
    idx.append(dict_plan[plan])


for i in idx:
    if x + dx[i] >= 0 and x + dx[i] <= n and y + dy[i] >= 0 and y + dy[i] <= n:
        x += dx[i]
        y += dy[i]
    
# 시작 위치가 1,1이기 때문에 1씩 더해준다.
x += 1
y += 1

# 출력
print(x,y, end=' ')

