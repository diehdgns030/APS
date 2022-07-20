# 문제
# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# words = list(map(int, input().split()))
# print(words)

# 입력예시
# I'm Tutor 6

# 출력예시
# ["I'm", 'Tutor', '6']

# 풀이
#int 형에서  str 형으로
words = list(map(str, input().split()))
print(words)