#문제
#문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
#count() 메서드 사용 금지

#입력예시
#apple

#출력예시
#1

#아래의 테스트 케이스로도 확인해보세요.
#banana  3
#kiwi  0

#풀이
word = input()
cnt = 0
for i in word:
    if i == 'a':
        cnt +=1
print(cnt)