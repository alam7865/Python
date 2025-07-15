import java.util.*;

public class sort {
    public static void main(String[] args) {
        int events[][] = { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 1, 2 } };
        int n = events.length;
        int day = 1;
        int res = 0;
        int i = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        while (i < n || !pq.isEmpty()) {
            // add all events at start at same day
            while (i < n && events[i][0] == day) {
                pq.add(events[i][1]);
                i++;
            }

            // remove expired events
            while (!pq.isEmpty() && pq.peek() < day) {
                pq.poll();
            }

            if (!pq.isEmpty()) {
                pq.poll();
                res++;
            }

            day++;
        }

        System.out.println("Result: " + res);
    }
}
