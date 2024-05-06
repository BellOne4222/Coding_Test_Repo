class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;
        int row = 0;
        int col = 0;
        int height = 0;
        
        row = box[0] / n;
        col = box[1] / n;
        height = box[2] / n;
        
        answer = row * col * height;
        
        return answer;
    }
}