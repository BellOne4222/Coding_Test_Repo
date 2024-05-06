import java.util.Arrays;

class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        int[] sortedArray = array.clone();
        
        // 배열을 정렬
        Arrays.sort(sortedArray);
        
        // 가장 큰 값을 answer[0]에 저장
        answer[0] = sortedArray[sortedArray.length - 1];
        
        // 원래 배열에서 가장 큰 값의 인덱스를 찾음
        for (int i = 0; i < array.length; i++) {
            if (array[i] == answer[0]) {
                answer[1] = i;
                break;
            }
        }
        
        return answer;
    }
}