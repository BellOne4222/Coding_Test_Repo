import java.util.*;

class Solution {
    public int[] solution(long n) {
        List<Long> answer = new ArrayList<>();
        
        while (n > 0) {
            answer.add(n % 10);  // 리스트의 맨 뒤에 추가
            n /= 10;
        }
        
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i).intValue();  // Long을 int로 변환
        }
        
        return result;
    }
}