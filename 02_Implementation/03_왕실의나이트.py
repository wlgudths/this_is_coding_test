# 나이트 위치 입력 받기
n = input()

# 카운트
cnt = 0

# 문자 idx 처리
dict_alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

# 시작위치 (0,0) ~ (7,7)
x,y = (int(n[1]) -1 , dict_alpha[n[0]])


# 방향 (총 8가지)
dx = [1,-1,1,-1,2,2,-2,-2]
dy = [2,2,-2,-2,1,-1,1,-1]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue
    
    cnt += 1


print(cnt)

