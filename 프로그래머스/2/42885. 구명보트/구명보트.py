def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    answer = 0
    while left <= right:
        answer += 1
        if limit - people[right] >= people[left]:
            left += 1
        right -= 1
    return answer