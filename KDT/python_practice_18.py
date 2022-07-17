#문제
#문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

#입력예시
#banana

#출력예시
#b 1
#a 3
#n 2

#풀이
word = input()#banana
result = {}#임의의 딕셔너리 생성
for i in word:#i에 banana를 하나씩 순회 대입
    if not i in result:
        result[i] = 1 
    else:
        result[i] += 1

for key in result:
    print(key, result[key])