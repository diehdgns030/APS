#문제
#문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
#모음 : a, e, i, o, u 
#count() 사용 금지

#입력예시
#apple

#출력예시
#2

#아래의 테스트 케이스로도 확인해보세요.
#aeiou  5
#zxcvb  0

#풀이
word = input()
vowel = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in word:
    for j in vowel:
        if i == j:
            cnt += 1
print(cnt)