class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        long cur_x = x;
        
        for(int i = 0; i < n; i++){
            answer[i] = cur_x;
            cur_x += x;
        }
        
        return answer;
    }
}