class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int pizza = (n / 7);
        int plus_pizza = (n % 7);
        
        if (plus_pizza > 0){
            pizza += 1;
        }
        
        answer += pizza;
        
        return answer;
    }
}