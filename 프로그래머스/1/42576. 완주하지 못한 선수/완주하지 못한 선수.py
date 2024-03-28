def solution(participant, completion):
    answer = ''
    hash_table = {}
    for person in participant:
        hash_table[person] = hash_table.get(person, 0) + 1
    for person in completion:
        hash_table[person] -= 1
    for person, count in hash_table.items():
        if count > 0:
            return person