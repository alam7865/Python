import java.util.*;

public class max3_min2 {
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 5 };
        int n = arr.length;
        int pos = 0;
        int neg = 0;
        int max1 = Integer.MIN_VALUE;
        int max2 = Integer.MIN_VALUE;
        int max3 = Integer.MIN_VALUE;

        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {

            if (max1 < arr[i]) {
                max3 = max2;
                max2 = max1;
                max1 = arr[i];
            } else if (max2 < arr[i]) {
                max3 = max2;
                max2 = arr[i];
            } else if (max3 < arr[i]) {
                max3 = arr[i];
            }
        }

        for (int i = 0; i < n; i++) {
            if (min1 > arr[i]) {
                min2 = min1;
                min1 = arr[i];
            } else if (min2 > arr[i]) {
                min2 = arr[i];
            }
        }

        // int prod1 = max1 * max2 * max3;
        // int prod2 = min1 * min2 * max1;

        // int max = Math.max(prod1, prod2);
        // System.out.println(prod1 + " " + prod2);
        // System.out.println("Product Max: " + max);

        System.out.println("MIN 1: " + min1 + " " + "MIN 2: " + min2);
        System.out.println("MAX 1: " + max1 + " " + "MAX 2: " + max2 + " " + "MAX3 :" + max3);
    }
}
