import java.util.*;

public class candy {
    public static void main(String[] args) {
        // int arr[] = { 3, 2, 1, 4 };
        int arr[] = { 3, 2, 1, 4, 5 };
        int low = 0;
        int high = arr.length - 1;
        // int k = 2;
        int k = 4;
        int sum1 = 0;
        Arrays.sort(arr);
        while (low <= high) {
            sum1 += arr[low++];

            int k1 = k;
            while (k1-- > 0) {
                if (high > low) {
                    // arr[high] = -1;
                    high--;
                } else {
                    break;
                }
            }
        }

        System.out.println(sum1);
    }
}
