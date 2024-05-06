class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        
        for (char c : my_string.toCharArray()) {
            if (Character.isUpperCase(c)) {
                char lowToUpper = Character.toLowerCase(c);
                answer.append(lowToUpper);
            } else if (Character.isLowerCase(c)) {
                char upToLower = Character.toUpperCase(c);
                answer.append(upToLower);
            } else {
                answer.append(c);
            }
        }
        
        return answer.toString();
    }
}
