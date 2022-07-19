#문제
#정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.
#0 <= a <= 10, 0 <= b <= 10

#입력예시
#1 3

#출력예시
#8

#풀이
a, b = map(int, input().split())
result = a * 2**b
print(result)