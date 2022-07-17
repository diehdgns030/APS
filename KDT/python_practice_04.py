#문제
#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

#Input : n = 5
#Output : 120

#풀이
#while 문
n = int(input())
cnt = 1
result = 1
while n >= cnt:
    result *= cnt
    cnt += 1
print(result)

#for 문
n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)