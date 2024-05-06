class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        char[] charArray = my_string.toCharArray();
        
        for (int i = charArray.length - 1; i >= 0; i--){
            answer += charArray[i];
        }
        
        return answer;
    }
}