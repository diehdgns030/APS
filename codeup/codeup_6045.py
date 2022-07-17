#문제
#정수 3개를 입력받아 합과 평균을 출력해보자.

#입력예시
#1 2 3

#출력예시
#6 2.00

#풀이
a, b, c = map(int, input().split(' '))
sum = a + b + c
average = sum / 3
print(sum, format(average,'.2f'))