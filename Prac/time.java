import java.util.*;

public class time {

    public static int toTime(String str) {
        int Hour = Integer.parseInt(str.substring(0, 2));
        int Min = Integer.parseInt(str.substring(3, 5));
        int Sec = Integer.parseInt(str.substring(6));
        int time = (Hour * 3600) + (Min * 60) + Sec;
        return time;
    }

    public static void main(String[] args) {
        String arr[] = { "00:00:05", "00:00:01", "23:59:59" };
        int n = arr.length;
        int time[] = new int[n];

        for (int i = 0; i < n; i++) {
            time[i] = toTime(arr[i]);
        }
        Arrays.sort(time);
        System.out.println(Arrays.toString(time));
        int Min_Time = Integer.MAX_VALUE;

        for (int i = 1; i < n; i++) {
            Min_Time = Math.min(Min_Time, time[i] - time[i - 1]);
        }

        int lTime = 86400 - time[n - 1] + time[0];
        Min_Time = Math.min(Min_Time, lTime);

        System.out.println("Result: " + Min_Time);
    }
}