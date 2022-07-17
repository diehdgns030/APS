#문제
#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
#sum() 함수 사용 금지

#Input : n = 10
#Ounput : 55

#풀이
#while문
n = int(input())
cnt = 0
result = 0
while n >= cnt:
    result += cnt
    cnt += 1
print(result)

#for문
n = int(input())
result = 0
for i in range(n + 1):
    result += i
print(result)