# 문제
# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# 입력예시
# x
# b
# k
# d
# l
# q
# g
# a
# c

# 출력예시
# x
# b
# k
# d
# l
# q

# 풀이
letter = ''
while letter != 'q':
    letter = input()
    print(letter)