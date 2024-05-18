T = int(input())
for test_case in range(1, T + 1):
    _ = input()
    numbers = list(map(int, input().split()))
    dic = {}
    for num in numbers:
        dic[num] = dic.get(num, 0) + 1
    max_count = max(dic, key=lambda k: (dic[k], k))
    print(f"#{test_case} {max_count}")
