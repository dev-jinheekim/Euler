# Problem 9

# 세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
# 예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.

# a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

def pythagoras(pytha_sum):
    """
    피타고라스 세 숫자의 합을 받아, 세 숫자를 추측하는 함수
    @sum:  a + b + c
    @return: a, b, c
    """

    for i in range(1, pytha_sum):
        for j in range(1, pytha_sum - i):
            if i ** 2 + j ** 2 == (pytha_sum - i - j) ** 2:
                return i, j, pytha_sum - i - j


a, b, c = pythagoras(1000)

print(a * b * c)
