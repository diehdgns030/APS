# 문제
# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
    
# 출력예시
# 두 번째 리스트의 최댓값이 더 큽니다.

#풀이
number_list = [1, 23, 9, 6, 91, 59, 29]
max_num1 = max(number_list)
# 예약어 max -> max_num로 변수명 변경

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max_num2 = max(number_list2)
# 예약어 max -> max_num로 변수명 변경

if max_num1 > max_num2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max_num1 < max_num2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")