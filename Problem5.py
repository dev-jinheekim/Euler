# Problem5

# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

def find_remainder_zero(div_range):
    flag = 2
    be_divisioned_number = 2

    while True:
        
        for i in range(2, div_range):
            if flag == div_range:
                return be_divisioned_number
            if result % i == 0:
                flag += 1
            else:
                be_divisioned_number += 1
                flag = 2

print(find_remainder_zero(20))


# FIXME: 속도가 오래걸리므로, 1~20을 소수로 만들어 계산하도록 재제작
