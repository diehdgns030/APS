# 문제
# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
# N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

# 입력
# 입력으로 정수 N 이 주어진다.


# 출력
# 정수 N 의 모든 약수를 오름차순으로 출력한다.

# 풀이
num = int(input())
a = range(1, num+1)
divisor = []
if num in range(1, 1001):
    for i in a:
        if num % i == 0:
            divisor.append(i)
            print(i, end=' ')
else:
    print('1 이상 1,000 이하의 정수를 입력해주세요')
        