class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;  // answer 변수를 조건문 밖에서 선언

        if (num1 == num2) {
            answer = 1;  // 조건에 맞으면 answer에 1 할당
        } else if (num1 != num2) {
            answer = -1;  // 그렇지 않으면 answer에 -1 할당
        }

        return answer;  // 최종적으로 answer 반환
    }
}
