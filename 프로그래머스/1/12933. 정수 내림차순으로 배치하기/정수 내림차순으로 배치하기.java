import java.util.*;

class Solution {
    public long solution(long n) {
        List<Long> lst = new ArrayList<>();
        
        while (n > 0) {
            lst.add(n % 10);
            n /= 10;
        }
        
        // 내림차순 정렬
        Collections.sort(lst, Collections.reverseOrder());
        
        long answer = 0;
        long multiplier = 1;
        
        // 리스트를 거꾸로 순회하면서 값을 계산
        for (long num : lst) {
            answer = answer * 10 + num;
        }
        
        return answer;
    }
}
