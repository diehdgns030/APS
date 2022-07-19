#문제
#2개의 정수값이 입력될 때,
#그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

#입력예시
#0 0

#출력예시
#True

#풀이
a, b = map(int, input().split())
if bool(a) == bool(b):
    print(True)
else:
    print(False)
