#문제
#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
#min() 함수 사용 금지

#입력예시
# numbers = [0, 20, 100]

#출력예시
# 0

#아래의 테스트 케이스로도 확인 해보세요.
#numbers = [0, 20, 100, 50, -60, 50, 100] # -60
#numbers = [0, 1, 0] # 0
#numbers = [-10, -100, -30] # -100

#풀이
numbers = [-10, -100, -30]
min = float('inf')
for i in numbers:
    if min > i:
        min = i
print(min)