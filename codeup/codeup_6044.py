#문제
#정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
#단, b는 0이 아니다.

#입력예시
#10 3

#출력예시
#13
#7
#30
#3
#1
#3.33

#풀이
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, '.2f'))