# 문제
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

# 입력예시
# A

# 출력예시
# best!!

# 풀이
letter = input()
if letter == 'A':
    print('best!!')
elif letter == 'B':
    print('good!!')
elif letter == 'C':
    print('run!')
elif letter == 'D':
    print('slowly~')
else:
    print('what?')
