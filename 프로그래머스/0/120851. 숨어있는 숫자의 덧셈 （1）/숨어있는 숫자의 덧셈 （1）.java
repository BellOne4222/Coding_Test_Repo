class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        for (char c : my_string.toCharArray()){
            if (Character.isDigit(c)){
                int charToInt = Character.getNumericValue(c);
                answer += charToInt;
            }
        }
        
        return answer;
    }
}