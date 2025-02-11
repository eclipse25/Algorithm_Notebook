def solution(nums):
    pkm = {}
    for num in nums:
        pkm[num] = pkm.get(num, 0) + 1
        
    answer = min(len(pkm), len(nums) // 2)
    return answer