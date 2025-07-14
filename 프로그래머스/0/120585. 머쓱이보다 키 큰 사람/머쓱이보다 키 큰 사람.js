function solution(array, height) {
    var answer = 0;
    
    let Array = array.filter((item) => item > height);
    
    answer = Array.length;
    
    return answer;
}