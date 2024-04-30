import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        LinkedList<Integer> result = new LinkedList<>();
        Queue<Integer> queue = new LinkedList<>();

        // Calculate days needed to finish each progress and push to queue
        for (int i = 0; i < progresses.length; i++) {
            int days = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
            queue.offer(days);
        }

        while (!queue.isEmpty()) {
            int current = queue.poll();
            int count = 1;

            while (!queue.isEmpty() && queue.peek() <= current) {
                count++;
                queue.poll();
            }

            result.add(count);
        }

        // Convert LinkedList to array
        return result.stream().mapToInt(i -> i).toArray();
    }
}