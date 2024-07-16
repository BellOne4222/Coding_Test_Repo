class Solution {
    public int solution(String s) {
        StringBuilder answer = new StringBuilder();
        
        char[] arr = s.toCharArray();
        
        for (char c : arr) {
            if (c == '-') {
                answer.append(c);
            } else if (c == '+') {
                continue;
            } else {
                answer.append(c);
            }
        }
        
        return Integer.parseInt(answer.toString());
    }
}
