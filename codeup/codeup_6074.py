# 문제
# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

# 입력예시
# f

# 출력예시
# a b c d e f

# 풀이
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1