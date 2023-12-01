# 입력 받기
n,m = map(int, input().split())

# 현재 위치와 바라보는 방향
a,b,d = map(int, input().split())

# 맵 생성
map = [list(map(int,input().split())) for _ in range(n)]

# 북동남서 방향
x = [-1,0,1,0]
y = [0,1,0,-1]


for i in range(n):
    for j in range(m):

        # 현재 위치 방문 처리
        map[a][b] = 2
        
        # 육지라면
        if map[i][j] == 0:
            # 4가지 방향 확인
            for i in range(len(x)):
                dx = a + x[i]
                dy = b + y[i]

                if map[dx][dy] != 1 and map[dx][dy] < 0 and map[dx][dy] <= n and map[dx][dy] <= m and map[dx][dy] != 2:
                    map[dx][dy] = 2


print(map)
    



            



