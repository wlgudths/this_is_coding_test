# 입력
n = int(input())

# 카운트
cnt = 0

# 시
for hour in range(0,n+1):
    # 분
    for min in range(0, 60):
        # 초
        for sec in range(0, 60):
            if '3' in str(hour) or '3' in str(min) or '3' in str(sec):
                cnt += 1

print(cnt)
