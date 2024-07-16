class Solution {
    public int solution(String num_str) {
        int answer = 0;
        
        for (char c : num_str.toCharArray()){
            int num = Character.getNumericValue(c);
            answer += num;
        }
        
        return answer;
    }
}
