# 문제
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

# 입력예시
# 73

# 출력예시
# B

# 풀이
num = int(input())
if num >= 90 and num <= 100:
    print('A')
elif num >= 70:
    print('B')
elif num >= 40:
    print('C')
else:
    print('D')