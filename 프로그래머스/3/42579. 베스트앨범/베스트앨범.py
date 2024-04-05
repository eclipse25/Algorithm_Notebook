def solution(genres, plays):
    answer = []
    count = {}
    songs = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        count[genre] = count.get(genre, 0) + play
        if genre not in songs:
            songs[genre] = []
        songs[genre].append([play, i])
    
    sorted_count = sorted(count.items(), key = lambda x:x[1], reverse = True)
    for element in sorted_count:
        genre = element[0]
        li = sorted(songs[genre], key = lambda x: (-x[0], x[1]))
        if len(li) >= 2:
            answer.append(li[0][1])
            answer.append(li[1][1])
        else:
            for i in range(len(li)):
                answer.append(li[i][1])
    return answer