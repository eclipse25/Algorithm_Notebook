import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = false;
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                stack.push(ch);
            } else if (!stack.empty() && ch == ')') {
                stack.pop();
            } else if (stack.empty() && ch == ')') {
                return false;
            }
        }
        
        if (stack.empty()) 
            answer = true;

        return answer;
    }
}