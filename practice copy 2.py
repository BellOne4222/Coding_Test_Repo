import java.util.Arrays;

class Solution {
    public int solution(int[] dots, int[] lines) {
        
        Arrays.sort(dots);
        
        Arrays.sort(lines);
        int n = lines.length;
        for (int i = 0; i < n / 2; i++) {
            int temp = lines[i];
            lines[i] = lines[n - 1 - i];
            lines[n - 1 - i] = temp;
        }

        int answer = 0; 
        int i = 0; 

        
        while (i < dots.length) {
            answer++; 
            int start = dots[i]; 

            
            for (int line : lines) {
                
                while (i < dots.length && dots[i] <= start + line) {
                    i++;
                }
                break;
            }
        }

        return answer;
    }
}