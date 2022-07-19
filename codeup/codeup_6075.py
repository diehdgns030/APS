# 문제
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

# 입력예시
# 4

# 출력예시
# 0
# 1
# 2
# 3
# 4

# 풀이
num = int(input())
cnt = 0
while num >= cnt:
    print(cnt)
    cnt += 1
