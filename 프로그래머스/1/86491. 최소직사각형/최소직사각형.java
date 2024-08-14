import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int max_side = 0;
        int min_side = 0;
        
        for (int i = 0; i < sizes.length; i++){
            if (sizes[i][0] > sizes[i][1]){
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
                
            } 
        }
        
        for (int j = 0; j < sizes.length; j++){
            min_side = Math.max(min_side, sizes[j][0]);
            max_side = Math.max(max_side, sizes[j][1]);
        }
        
        answer = min_side * max_side;
        
        
        
        return answer;
    }
}