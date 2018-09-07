# Problem 7

# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

# 이 때 10,001번째의 소수를 구하세요.

def decimal_check(number):
    """
    숫자를 입력받아 소수인지 체크하는 함수
    @number: int
    @return: boolean
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False;
    return True


def decimal(number):
    """
    입력받은 숫자보다 작은 소수들을 리턴하는 함수
    @number: int
    @return: list
    """
    decimal_list = []
    for i in range(number):
        if decimal_check(i):
            print(i)
            decimal_list.append(i)
    
    return decimal_list


def pick_decimal(number):
    """
    입력받은 숫자번째의 소스를 리턴하는 함수
    @number: int
    @reutrn: int
    """
    flag = 0
    decimal_list = []
    for i in range(10000000):
        if flag == number:
            break
        if decimal_check(i):
            decimal_list.append(i)
            flag += 1

    return decimal_list[number-1]


print(pick_decimal(10001))

# problem 10 
# print(sum(decimal(2000000)))

