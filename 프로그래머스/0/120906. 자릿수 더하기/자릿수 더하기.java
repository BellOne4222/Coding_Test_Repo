class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String numToString = String.valueOf(n);
        
        char[] charArray = numToString.toCharArray();
        
        for (char c : charArray){
            answer += Character.getNumericValue(c);
        }
        
        return answer;
    }
}