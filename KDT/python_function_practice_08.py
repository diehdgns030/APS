# 문제
# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# 출력예시
# 3

# 풀이
#0또는 False를 제외한 값은 모두 True
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char ==  "o" or char ==  "u": 
        count += 1

print(count)