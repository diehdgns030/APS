#문제
#2개의 정수값이 입력될 때,
#그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

#입력예시
#1 1

#출력예시
#True

#풀이
a, b = map(int, input().split(' '))
if bool(a) == True and bool(b) == True:
    print(True)
else:
    print(False)