import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        String numToStr = Integer.toString(n);
        
        String[] strToList = numToStr.split("");
        
        for (int i = 0; i < strToList.length; i++){
            int num = Integer.parseInt(strToList[i]);
            answer += num;
        }

        return answer;
    }
}