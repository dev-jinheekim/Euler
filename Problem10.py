# Problem 10 

# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

# problem 7을 재활용 하여 풀었으나, 시간이 너무 오래걸림 




# 모법 답안 
# 에라토스테네스의 체


# 결과 값을 저장하는 목록을 미리 생성한다.
result = []
#전체 범위를 지정한다. : 1은 소수임을 알고 있으므로 제외하고 2부터 수행해야 하지만 초기값은 별도로 생성할 것이므로 3부터 999까지의 범위로 한다.
candidates = range(3,1000)
#초기값을 설정한다.
base = 2
#초기값의 배수를 구하기 위한 임시 변수를 생성한다.
product = base

#전체 범위 내에서 "에라토스테네스의 체" 알고리즘을 수행한다.
while candidates:
    #임시변수가 1000미만일 때까지 다음을 수행한다.
    while product < 1000:
        #임시변수가 전체 범위내 존재한다면 :
        if product in candidates:
            #전체 범위 목록에서 임시변수를 삭제한다.
            candidates.remove(product)
            #임시변수는 기본값의 배수이다.
            product = product+base
        #결과 목록에 기본값을 추가한다.
        result.append(base)
        #다음 기본값은 (이미 걸러진)전체 목록의 첫 번째 값이다. : 1회 걸렀을 경우 2와 2의 배수를 모두 삭제했으므로 3이다.
        base = candidates[0]
        #초기값의 배수를 구하기 위해 임시 변수를 다시 생성한다.
        product = base
        #전체 범위에서 초기값을 제거한다.
        del candidates[0]
    # 범위 내의 마지막 기본값을 결과 목록에 추가한다.
    result.append(base)
    #결과 목록을 화면에 출력한다.
    print result

