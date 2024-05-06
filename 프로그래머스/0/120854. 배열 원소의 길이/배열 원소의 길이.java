class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        int idx = 0;
        
        
        for (String str : strlist){
            int length = str.length();
            answer[idx] = length;
            idx++;
        }
        
        return answer;
    }
}