import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] nums = new String[numbers.length];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(nums, new Comparator<String>() {
            public int compare(String a, String b) {
                return (b + b + b).compareTo(a + a + a);
            }
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