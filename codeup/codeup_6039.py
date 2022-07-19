#문제
#실수 2개(f1, f2)를 입력받아
#f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

#Input
#4.0 2.0

#Output
#16.0

#풀이
f1, f2 = input().split()
result = float(f1)**float(f2)
print(result)