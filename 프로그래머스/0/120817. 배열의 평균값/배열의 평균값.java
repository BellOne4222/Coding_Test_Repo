class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        double sum = 0.0;
        
        for (double num : numbers){
            sum += num;
        }
        
        answer = sum / numbers.length; 
        
        return answer;
    }
}