class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;

        // str1 내에서 str2와 일치하는 부분 문자열이 있는지 확인
        for (int i = 0; i < str1.length() - str2.length() + 1; i++) {
            String compare = str1.substring(i, i + str2.length());
            if (compare.equals(str2)) {
                answer = 1;
                break;
            }
        }

        // str2가 str1 내에 없다면 answer를 2로 설정
        if (answer == 0) {
            answer = 2;
        }

        return answer;
    }
}
