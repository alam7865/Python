import java.util.*;

public class coinPile {
    public static void main(String[] args) {
        int arr[] = { 2, 2, 2, 2 };
        int k = 0;
        int n = arr.length;
        int prefixSum[] = new int[n];
        prefixSum[0] = arr[0];

        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }

        int minANS = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int base = arr[i];
            int maxAllowed = base + k;

            int low = i;
            int high = n - 1;
            int idx = n;

            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (arr[mid] >= maxAllowed) {
                    idx = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }

            int removeLeft = (i > 0) ? prefixSum[i - 1] : 0;
            // remove right
            int rightCount = n - idx;
            int sumRight = 0;
            if (idx < n) {
                sumRight = (idx > 0) ? (prefixSum[n - 1] - prefixSum[idx - 1]) : prefixSum[n - 1];
            }
            int removeRight = sumRight - (int) (rightCount * maxAllowed);
            int totalRemove = removeLeft + removeRight;
            minANS = Math.min(minANS, totalRemove);
        }

        System.out.println(minANS);

    }
}
