#문제
#숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
#cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

#입력예시
#12

#출력예시
#1728

def cube(a):
    return a**3

n = int(input())
print(cube(n))