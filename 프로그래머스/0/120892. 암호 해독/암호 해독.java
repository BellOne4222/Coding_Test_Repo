class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        char[] lst = cipher.toCharArray();
        
        // code 간격으로 문자를 가져오기 위해 인덱스를 증가
        for (int i = code - 1; i < lst.length; i += code) {
            answer += lst[i];
        }
        
        return answer;
    }
}
