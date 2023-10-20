package onboarding;

import java.util.List;

class Problem1 {
    // 게임 결과를 계산하는 메소드
    public static int solution(List<Integer> pobi, List<Integer> crong) {
        int pobiScore;   // pobi의 게임 결과 점수
        int crongScore;  // crong의 게임 결과 점수

        // 게임을 시작할 수 있는지 확인하고, 불가능하면 -1을 반환하고 게임을 종료
        if (!canGameStart(pobi, crong)) return -1;

        // pobi와 crong의 각각의 카드 점수를 계산하고, 최대값을 pobiScore와 crongScore에 저장
        pobiScore = Math.max(howManyScore(pobi.get(0)), howManyScore(pobi.get(1)));
        crongScore = Math.max(howManyScore(crong.get(0)), howManyScore(crong.get(1)));

        // 게임 결과를 반환
        return gameResult(pobiScore, crongScore);
    }

    // 게임을 시작할 수 있는지 확인하는 메소드
    private static boolean canGameStart(List<Integer> pobi, List<Integer> crong) {
        // 예외 상황 검사를 통과하면 게임 시작 가능
        return exceptionCheck(pobi.get(0), pobi.get(1)) && exceptionCheck(crong.get(0), crong.get(1));
    }

    // 예외 상황 검사를 하는 메소드
    private static boolean exceptionCheck(int num1, int num2) {
        // 범위, 연속성, 페이지 번호의 조건을 모두 만족해야 함
        return isRightRange(num1, num2) && isNumberContinuous(num1, num2) && isRightPage(num1, num2);
    }

    // 숫자의 범위를 검사하는 메소드
    private static boolean isRightRange(int num1, int num2) {
        return 1 <= num1 && num2 <= 400;
    }

    // 숫자가 연속성을 가지는지 검사하는 메소드
    private static boolean isNumberContinuous(int num1, int num2) {
        return num1 + 1 == num2;
    }

    // 페이지 번호가 올바른지 검사하는 메소드
    private static boolean isRightPage(int num1, int num2) {
        return num1 % 2 == 1 && num2 % 2 == 0;
    }

    // 게임 결과를 계산하는 메소드
    private static int gameResult(int pobiScore, int crongScore) {
        // pobiScore와 crongScore를 비교하여 승자를 결정하고 반환
        if (pobiScore > crongScore) return 1;
        if (pobiScore < crongScore) return 2;
        return 0; // 무승부
    }

    // 숫자의 점수를 계산하는 메소드
    private static int howManyScore(int num) {
        // 각 자릿수의 합 또는 곱셈 결과 중 더 큰 값을 반환
        return Math.max(plusDigits(num), multiFlyDigits(num));
    }

    // 숫자의 각 자릿수를 더하는 메소드
    private static int plusDigits(int num) {
        if (num >= 100) {
            return num / 100 + ((num % 100) / 10) + num % 10;
        }
        return num / 10 + num % 10;
    }

    // 숫자의 각 자릿수를 곱하는 메소드
    private static int multiFlyDigits(int num) {
        if (num >= 100) {
            return (num / 100) * ((num % 100) / 10) * (num % 10);
        }
        return (num / 10) * (num % 10);
    }
}