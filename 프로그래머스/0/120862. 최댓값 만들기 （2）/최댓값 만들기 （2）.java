import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        // 배열 정렬
        Arrays.sort(numbers);

        // 배열에서 가장 큰 두 양수의 곱 계산
        int maxProduct = numbers[numbers.length - 1] * numbers[numbers.length - 2];

        // 배열에서 가장 작은 두 음수의 곱 계산
        int minProduct = numbers[0] * numbers[1];

        // 최댓값 반환
        return Math.max(maxProduct, minProduct);
    }
}
