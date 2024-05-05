class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int sheep = 12000;
        int beverage = 2000;
        int discount = n / 10;
        
        answer = (sheep * n) + (beverage * (k - discount));
        
        return answer;
    }
}