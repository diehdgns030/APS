# 문제
# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# 입력예시
# 123 456

# 출력예시
# 456

# 풀이
a, b = map(int, input().split())
if a < b:
    print(b)
elif a == b:
    print('a와 b의 값이 같습니다.')
elif a > b:
    print(a)
