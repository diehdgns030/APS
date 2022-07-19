#문제
#단어와 반복 횟수를 입력받아 여러 번 출력해보자.

#Input
#love 3

#Output
#lovelovelove

#풀이
a, b = input().split()
result = a * int(b)
print(result)