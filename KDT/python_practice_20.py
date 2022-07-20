# #문제
# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

# 입력예시
# 123

# 출력예시
# 6

#풀이
num = 347
cnt = 0

while (num > (10**cnt)):
    cnt += 1
num_len = cnt 

total_sum = 0

while(num_len >= 0):
    cnt_2 = 0

    while (num > (10**num_len) or num == 1):  
        num -= (10**num_len)
        cnt_2 += 1 
    
    total_sum += cnt_2
    num_len -= 1
    