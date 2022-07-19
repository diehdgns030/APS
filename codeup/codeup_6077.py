# 문제
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 입력예시
# 5

# 출력예시
# 6

# 풀이
num = int(input())
sum_even = 0
cnt = 0
while num >= cnt:#넘버가 더 크면 아래 조건문 실행
    if cnt %2 == 0:#만약 cnt가 짝수면
        sum_even += cnt# 합계에 더 그수를 더함
    cnt += 1


print(sum_even)#맞음