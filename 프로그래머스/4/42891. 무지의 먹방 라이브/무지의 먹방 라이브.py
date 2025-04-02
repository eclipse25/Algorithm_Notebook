import heapq

def solution(food_times, k):
    # 모든 음식을 먹는데 필요한 시간이 k보다 작거나 같으면 더 이상 먹을 음식이 없으므로 -1 반환
    if sum(food_times) <= k:
        return -1

    # 음식 시간과 인덱스를 튜플로 묶어 최소 힙에 추가
    food_heap = [(time, i) for i, time in enumerate(food_times, start=1)]
    heapq.heapify(food_heap)

    total_time = 0  # 누적된 시간
    prev_time = 0
    while food_heap:
        # 가장 적게 남은 음식을 모두 먹는데 걸리는 시간(그동안 다른 음식들도 같은 양만큼 먹음)
        curr_time = (food_heap[0][0] - prev_time) * len(food_heap)
        if total_time + curr_time > k: 
            # 이번 사이클(모든 음식에서 동일한 시간만큼 먹는 것)을 끝내기 전에 k초가 도달한 경우
            # 인덱스 순으로 남은 음식 정렬
            index_sorted_foods = sorted(food_heap, key=lambda x: x[1])
            # k초 후에 먹어야 하는 음식의 인덱스를 반환
            return index_sorted_foods[(k - total_time) % len(food_heap)][1]
        # 현재 음식을 모두 먹고 다음 음식으로 넘어감
        total_time += curr_time
        prev_time, _ = heapq.heappop(food_heap) # 각 음식이 지금까지 먹힌 횟수
        
    return -1
        