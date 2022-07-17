#문제
#정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

#Input
#123 -123

#Output
#246

#풀이

a, b = input().split(' ')
result = int(a) - int(b)
print(result)