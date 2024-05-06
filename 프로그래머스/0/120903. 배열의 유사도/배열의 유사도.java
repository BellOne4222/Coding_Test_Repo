class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        
        for (String c1 : s1){
            for (String c2 : s2){
                if (c1.equals(c2)){
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
}