# Problem 2

# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
# 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

fibonacci = [1, 2]
result = 0

for i in range(1, 100):
    next_fibonacci = fibonacci[i-1] + fibonacci[i]
    if next_fibonacci >= 4000000:
        for i in fibonacci:
            if i % 2 == 0:
                result += i      
        print('결과값')
        print(result)
    fibonacci.append(next_fibonacci)

print(fibonacci)
