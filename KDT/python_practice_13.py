#문제
#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

#입력예시
#apple

#출력예시
#elppa

#풀이1
word = input()
print(word[::-1])

#풀이2
result = ''
for i in word:
    result = i + result
print(result)