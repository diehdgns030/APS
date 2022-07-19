# 문제
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# 입력예시
# 3 -1 5

# 출력예시
# -1

#풀이
a, b, c = map(int, input().split())  
if a < b and b <= c:
    print(a)
elif b < a and a <= c:
    print(b)
else:
    print(c)