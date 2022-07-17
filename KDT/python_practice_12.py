#문제
#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

#입력예시
#apple

#출력예시
#pple

#풀이
word = input()
result = ''
for i in word:
    if i != 'a':
        result += i
print(result)