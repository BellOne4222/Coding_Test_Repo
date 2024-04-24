import java.util.*;

public class Main {
    static class Gear {
        private int[] teeth = new int[8];
        
        public Gear(String config) {
            for (int i = 0; i < 8; i++) {
                teeth[i] = config.charAt(i) - '0';
            }
        }
        
        public void rotate(int direction) {
            if (direction == 1) { // Clockwise rotation
                int last = teeth[7];
                for (int i = 7; i > 0; i--) {
                    teeth[i] = teeth[i - 1];
                }
                teeth[0] = last;
            } else if (direction == -1) { // Counterclockwise rotation
                int first = teeth[0];
                for (int i = 0; i < 7; i++) {
                    teeth[i] = teeth[i + 1];
                }
                teeth[7] = first;
            }
        }
        
        public int get(int position) {
            return teeth[position];
        }
    }
    
    private static void rotateGears(List<Gear> gears, int wheelNum, int direction) {
        int[] rotate = new int[gears.size()];
        rotate[wheelNum - 1] = direction;
        
        // Check rotations to the left
        for (int i = wheelNum - 1; i > 0; i--) {
            if (gears.get(i).get(6) != gears.get(i - 1).get(2)) {
                rotate[i - 1] = -rotate[i];
            } else {
                break;
            }
        }
        
        // Check rotations to the right
        for (int i = wheelNum - 1; i < gears.size() - 1; i++) {
            if (gears.get(i).get(2) != gears.get(i + 1).get(6)) {
                rotate[i + 1] = -rotate[i];
            } else {
                break;
            }
        }
        
        // Apply rotations
        for (int i = 0; i < gears.size(); i++) {
            gears.get(i).rotate(rotate[i]);
        }
    }
    
    private static int calculateScore(List<Gear> gears) {
        int score = 0;
        int[] points = {1, 2, 4, 8};
        for (int i = 0; i < gears.size(); i++) {
            if (gears.get(i).get(0) == 1) {
                score += points[i];
            }
        }
        return score;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Gear> gears = new ArrayList<>();
        
        for (int i = 0; i < 4; i++) {
            String input = scanner.next();
            gears.add(new Gear(input));
        }
        
        int k = scanner.nextInt();
        for (int i = 0; i < k; i++) {
            int wheelNum = scanner.nextInt();
            int direction = scanner.nextInt();
            rotateGears(gears, wheelNum, direction);
        }
        
        System.out.println(calculateScore(gears));
        scanner.close();
    }
}
