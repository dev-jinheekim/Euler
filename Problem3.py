# Problem 3

# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.
# 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

fraction = []

def partial_fraction_decomposition(target_number):
    for i in range(2, target_number + 1):
        if i == target_number:
            fraction.append(i)
            return 0
        if target_number % i == 0:
            fraction.append(i)
            return int(target_number / i)

result = partial_fraction_decomposition(600851475143)

while result != 0: 
    result = partial_fraction_decomposition(result)

print(fraction.pop())
