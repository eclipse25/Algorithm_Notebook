def make_palindrome(left: int, odd: bool):
    left_str = str(left)
    if odd:
        return int(left_str + left_str[-2::-1])  # 가운데 수 하나 제외하고 뒤집음
    else:
        return int(left_str + left_str[::-1])    # 그대로 뒤집음


def next_palindrome(n: int) -> int:
    length = len(str(n))
    odd = length % 2 == 1
    half_length = (length + 1) // 2
    left = int(str(n)[:half_length])

    pal = make_palindrome(left, odd)
    if pal > n:
        return pal

    left += 1
    if len(str(left)) > half_length:
        length += 1
        odd = length % 2 == 1
        half_length = (length + 1) // 2
        left = 10**(half_length - 1)

    return make_palindrome(left, odd)
        
n = int(input())
print(next_palindrome(n))
