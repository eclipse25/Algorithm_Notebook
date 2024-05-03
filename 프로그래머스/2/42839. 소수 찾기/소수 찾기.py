from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # 6k, 6k+2, 6k+3, 6k+4는 소수가 아니다.
        i += 6
    return True

def solution(numbers):
    num_set = set()
    
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num = int(''.join(perm))
            num_set.add(num)
            
    answer = 0
    for num in num_set:
        if is_prime(num):
            answer += 1
    return answer