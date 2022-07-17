#문제
# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수를 바로 쓰기보다는 반복문을 활용하세요.

#입력예시
# word = 'happy!'

#출력예시
# 6

#풀이
word = input()
cnt = 0
for i in word:
    cnt += 1
print(cnt)