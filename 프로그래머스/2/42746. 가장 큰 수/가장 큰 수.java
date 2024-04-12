import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] nums = new String[numbers.length];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(nums, (a, b) -> {
            String as = String.valueOf(a);
            String bs = String.valueOf(b);
            return -Integer.compare(Integer.parseInt(as + bs), Integer.parseInt(bs + as));
        });
        
        for (String num : nums) {
            answer += num;
        }
        
        if (answer.charAt(0) == '0') {
            answer = "0";
        }
        return answer;
    }
}