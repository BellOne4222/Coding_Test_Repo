import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        int sum = 0;
        int answer = 0;
        
        sum = sides[0] + sides[1];
        
        if (sum > sides[2]){
            answer = 1;
        } else if (sum <= sides[2]){
            answer = 2;
        }
        
        return answer;
    }
} 