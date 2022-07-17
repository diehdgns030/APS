#문제
#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.

#Input : numbers = [0, 20, 100]
#Output : 20

#아래의 테스트 케이스로도 확인 해보세요.
#numbers = [0, 20, 100, 50, -60, 50, 100] # 50
#numbers = [0, 1, 0] # 0
#numbers = [-10, -100, -30] # -30

#풀이
from re import A


numbers = [200, 20, 100]
max = float('-inf')
second_number = float('-inf')
for i in numbers:
    if max < i:
        second_number = max
        max = i
    elif max > i and i > second_number:
        second_number = i
print(second_number)