import java.util.HashSet;
import java.util.Set;

class Solution {
    public String solution(String my_string) {
        StringBuilder answerBuilder = new StringBuilder();
        String moeum = "aeiou";
        
        // 모음 집합을 생성
        Set<Character> moeumSet = new HashSet<>();
        for (char vowel : moeum.toCharArray()) {
            moeumSet.add(vowel);
        }
        
        // 입력 문자열을 문자 배열로 변환
        char[] charArray = my_string.toCharArray();
        
        // 모음이 아닌 문자를 결과에 추가
        for (char c : charArray) {
            if (moeumSet.contains(c)) {
                continue;
            } else {
                answerBuilder.append(c);
            }
        }
        
        // 최종 결과를 문자열로 변환
        String answer = answerBuilder.toString();
        
        return answer;
    }
}
