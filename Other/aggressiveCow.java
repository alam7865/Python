import java.util.*;

public class aggressiveCow {

    public static boolean isPossible(int mid, int cow, int arr[]) {
        int lastCowPos = arr[0];
        cow--;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - lastCowPos >= mid) {
                lastCowPos = arr[i];
                cow--;
            }

            if (cow == 0) {
                return true;
            }
        }
        return false;

    }

    public static void main(String[] args) {
        int arr[] = { 10, 1, 2, 7, 5 };
        int k = 3;
        int n = arr.length;

        if (k > n) {
            System.out.println("False");
        }

        Arrays.sort(arr);
        int low = 1;
        int high = arr[n - 1];
        int ans = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (isPossible(mid, k, arr)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        System.out.println("Result: " + ans);
    }
}
