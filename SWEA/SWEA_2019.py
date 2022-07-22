# 문제
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

# 풀이
num = int(input())
if num in range(1, 31):
    a = range(num+1)
    for i in a:
        print(1*2**i, end=' ')
else:
    print('1 이상 30 이하의 정수를 입력해주세요.')