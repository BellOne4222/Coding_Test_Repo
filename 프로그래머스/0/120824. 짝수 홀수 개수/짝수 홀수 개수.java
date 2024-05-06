class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int jjack = 0;
        int hole = 0;
        
        
        for (int num : num_list){
            if (num % 2 == 0){
                jjack += 1;
            } else if (num % 2 != 0){
                hole += 1;
            }
        }
        
        answer[0] = jjack;
        answer[1] = hole;
        
        return answer;
    }
}