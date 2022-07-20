# #문제
# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

# 입력예시
# 1234

# 출력예시
# 4321

# 풀이
num = 3947
cnt = 0

while (num > (10**cnt)):
    cnt += 1
num_len = cnt 

num_list = []

while(num_len >= 0):
    cnt_2 = 0 

    while (num > (10**num_len) or num == 1):  
        num -= (10**num_len)
        cnt_2 += 1 
    
    num_list.append(cnt_2)
    num_len -= 1

num_len2 = cnt

for i in range(1,num_len2+1):
    print(num_list[-i],end='')