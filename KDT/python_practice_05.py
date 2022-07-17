#문제
#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지**

#Input : numbers = [3, 10, 20]
#Output : 11.0

#풀이
numbers = [3, 10, 20]
cnt = 0
result = 0
for i in numbers:
    cnt += 1
    result += i
average = result/cnt
print(average)