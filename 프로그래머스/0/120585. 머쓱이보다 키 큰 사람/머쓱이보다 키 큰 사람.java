class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        
        for (int num : array){
            if (height < num){
                answer += 1;
            }
        }
        
        return answer;
    }
}