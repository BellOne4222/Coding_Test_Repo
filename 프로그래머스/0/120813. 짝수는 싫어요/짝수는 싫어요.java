import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        List<Integer> oddNumbers = new ArrayList<>();

        // 홀수만 리스트에 추가
        for (int i = 1; i <= n; i += 2) {
            oddNumbers.add(i);
        }

        // 리스트를 배열로 변환
        int[] answer = new int[oddNumbers.size()];
        for (int i = 0; i < oddNumbers.size(); i++) {
            answer[i] = oddNumbers.get(i);
        }

        return answer;
    }
}
