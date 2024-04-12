import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        ArrayList<Integer> completed = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        Queue<Integer> bridge = new LinkedList<>();
        
        for (int truck : truck_weights) {
            queue.add(truck);
        }
        
        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }
        
        int time = 0, weight_sum = 0;
        while (truck_weights.length > completed.size()) {
            time++;
            int removed = bridge.poll(); //null이 아님
            if (removed != 0) {
                completed.add(removed);
                weight_sum -= removed;
            }
            
            Integer new_truck = queue.peek(); //null일 수 있음
            if ((new_truck != null) && (weight_sum + new_truck <= weight)) {
                queue.poll();
                bridge.add(new_truck);
                weight_sum = weight_sum + new_truck;
            } else {
                bridge.add(0);
            }
        }
        return time;
    }
}