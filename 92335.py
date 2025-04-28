
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    # Step 1. n을 k진수로 변환
    tmp = ''
    while n > 0:
        tmp = str(n % k) + tmp
        n = n // k

    # Step 2. 변환된 문자열을 '0'으로 분리
    arr = tmp.split('0')

    # Step 3. 소수 판별
    count = 0
    for a in arr:
        if a:  # 빈 문자열이 아니고
            if is_prime(int(a)):
                count += 1

    return count
