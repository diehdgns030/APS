#문제
#문자 1개를 입력받아 그 다음 문자를 출력해보자.
#영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

#Input
#a

#Output
#b

#풀이
a = input()
new_a = ord(a) + 1
print(chr(new_a))