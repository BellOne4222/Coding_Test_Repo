import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n, int[] numlist) {
        // 결과를 일시적으로 저장할 리스트를 초기화
        List<Integer> resultList = new ArrayList<>();
        
        // numlist를 순회하며 조건에 맞는 값을 리스트에 추가
        for (int num : numlist) {
            if (num % n == 0) {
                resultList.add(num);
            }
        }
        
        // 리스트를 배열로 변환
        int[] answer = resultList.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}
