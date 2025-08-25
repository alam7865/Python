import java.util.*;

public class minimumPage {
    public static boolean IsPossible(int arr[], int mid, int k) {
        int count = 1;
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > mid) {
                return false;
            }

            if (sum + arr[i] <= mid) {
                sum += arr[i];
            } else {
                count++;
                sum = arr[i];
            }
        }

        if (count == k) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        int arr[] = { 12, 34, 67, 90 };
        int k = 2;

        int low = 0;
        int high = 1000;
        int ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (IsPossible(arr, mid, k)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        System.out.println("Result: " + ans);
    }
}