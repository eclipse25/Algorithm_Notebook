import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> cl = new HashMap<>();
        
        for (int i = 0; i < clothes.length; i++) {
            String type = clothes[i][1];
            cl.put(type, cl.getOrDefault(type, 0) + 1);
        }
        
        int answer = 1;
        for (int value : cl.values()) {
            answer *= (value + 1);
        }
        answer -= 1;
        
        return answer;
    }
}