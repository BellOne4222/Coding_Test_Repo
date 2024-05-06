class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        
        int length = num2 - num1 + 1;
        
        int[] answer = new int[length];
        int idx = 0;
        
        for (int i = num1; i < num2 + 1; i++){
            answer[idx] = numbers[i];
            idx++;
        }
        
        return answer;
    }
}