#문제
#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

#Input
#2020.3.4

#Output
#4-3-2020

#풀이
y, m, d = input().split('.')
print(d, m, y, sep='-')