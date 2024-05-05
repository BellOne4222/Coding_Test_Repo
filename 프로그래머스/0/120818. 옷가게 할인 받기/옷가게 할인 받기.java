class Solution {
    public int solution(int price) {
        double discount = 0.0;

        // 큰 값부터 작은 값 순으로 조건문 정렬
        if (price >= 500000) {
            discount = 0.2;
        } else if (price >= 300000) {
            discount = 0.1;
        } else if (price >= 100000) {
            discount = 0.05;
        }

        // 계산된 최종 금액을 int로 변환하여 반환
        int answer = (int) (price * (1 - discount));

        return answer;
    }
}
