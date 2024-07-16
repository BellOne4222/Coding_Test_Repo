class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int p_cnt = 0;
        int y_cnt = 0;
        
        String changedStr = s.toLowerCase();
        
        for (char c : changedStr.toCharArray()){
            if (c == 'p'){ // 'p'를 문자 리터럴로 사용
                p_cnt += 1;
            } else if (c == 'y'){ // 'y'를 문자 리터럴로 사용
                y_cnt += 1;
            }
        }
        
        if (p_cnt != y_cnt){
            answer = false;
        } 

        return answer;
    }
}
