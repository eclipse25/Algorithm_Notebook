import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        
        int answer = 0;
        Queue<int[]> queue = new LinkedList<>();
        ArrayList<int[]> sequence = new ArrayList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            int[] pair = {i, priorities[i]};
            queue.add(pair);
        }
        
        while (!queue.isEmpty()) {
            int[] element = queue.remove();
            boolean flag = false;
            for (int[] array : queue) {
                if (array[1] > element[1]) {
                    flag = true;
                    break;
                }
            }
            if (flag) {
                queue.add(element);
            } else {
                sequence.add(element);
                if (element[0] == location) {
                    answer = sequence.size();
                    break;
                }
            }
        }
        
        return answer;
    }
}