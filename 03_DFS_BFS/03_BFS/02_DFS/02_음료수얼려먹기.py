# 정답 1회 본 후 다시 풀어보기

# N,M 입력 받기
N,M = map(int, input().split())


# 2차원 리스트
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x,y):
    # 범위를 벗어나는 경우 종료
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False
    
    # 현재 노드를 방문하지 않을 경우
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1

        # 상,하,좌,우 재귀적으로 호출
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    
    return False
    

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)
