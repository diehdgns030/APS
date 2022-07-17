#문제
#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#.upper(), .swapcase() 사용 금지

#입력예시
#banana

#출력예시
#BANANA

#풀이
word = input()
upper_word = ''
for i in word:
    upper_word += chr(ord(i)-32)
print(upper_word)