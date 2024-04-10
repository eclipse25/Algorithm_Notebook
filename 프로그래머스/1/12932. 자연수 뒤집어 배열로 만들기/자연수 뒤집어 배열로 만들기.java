import java.util.ArrayList;

class Solution {
    public int[] solution(long n) {
        String[] digits = String.valueOf(n).split("");
        
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = digits.length - 1; i >= 0; i--) {
            result.add(Integer.parseInt(digits[i]));
        }
        
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}