#문제
#정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

#Input
#10 3

#Output
#3

#풀이
a, b = input().split()
share = int(a) // int(b)
print(share)