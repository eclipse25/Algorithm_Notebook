def solution(keymap, targets):
    answer = []
    max_key_len = max(len(key) for key in keymap)
    # 문자열개수
    for i in range(len(targets)):
        result = 0
        # 알파벳 개수만큼 반복
        for j in range(len(targets[i])):
            # 입력할 수 없는 알파벳 존재 여부
            fail = 0
            # 일치하는 알파벳을 찾을 때까지 반복
            for k in range(max_key_len):
                # 최소횟수 찾았는지 여부
                found = 0
                # key 개수만큼 반복
                for l in range(len(keymap)):
                    # key의 길이가 k보다 짧으면 패스
                    if len(keymap[l]) < k + 1:
                        continue
                    # key의 길이가 k보다 길면 탐색
                    if targets[i][j] == keymap[l][k]:
                        found = 1
                        result += (k + 1)
                        break
                if found == 1:
                    break
            # 알파벳이 하나라도 존재하지 않으면 중단
            if found == 0:
                fail = 1
                break
        if fail == 1:
            result = -1
        answer.append(result)
    return answer
