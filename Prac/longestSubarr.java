import java.util.*;

public class longestSubarr {
    public static void main(String[] args) {
        // int arr[] = { 0, 1, 1, 1, 0, 1, 1, 0, 1 };

        // int n = arr.length;
        // int max = 0;
        // int count = 0;
        // int key = -1;
        // int prevCount = 0;
        // // int max=0;
        // HashMap<Integer, int[]> map = new HashMap<>();

        // for (int i = 0; i < n; i++) {
        // if (arr[i] == 1) {
        // count++;
        // } else {
        // // when encounter 0
        // if (map.size() > 1) {
        // map.put(key, new int[] { prevCount, count });
        // }
        // map.put(i, new int[] { prevCount, count });
        // int sum = prevCount + count;
        // max = Math.max(max, sum);
        // prevCount = count; // update for next zero
        // count = 0; // reset
        // key = i;

        // }
        // }

        // for (Map.Entry<Integer, int[]> set : map.entrySet()) {
        // int keys = set.getKey();
        // int arr1[] = set.getValue();
        // int sum1 = 0;
        // for (int i = 0; i < arr1.length; i++) {
        // sum1 += arr1[i];
        // }

        // System.out.println(keys + " " + Arrays.toString(arr1) + " " + sum1);
        // }

        // /////////////////////////////////////////////////////////////////////////////////////////////////

        // int arr[] = {0, 1, 1, 1, 0, 1, 1, 0, 1};
        // int n = arr.length;
        // int count = 0;
        // int prevCount = 0;
        // int max = 0;

        // HashMap<Integer, int[]> map = new HashMap<>();

        // for (int i = 0; i < n; i++) {
        // if (arr[i] == 1) {
        // count++;
        // } else {
        // // when we hit a zero
        // map.put(i, new int[]{prevCount, count});
        // max = Math.max(max, prevCount + count);
        // prevCount = count; // update left streak
        // count = 0; // reset right streak
        // }
        // }

        // // if no zero in array -> must delete one element
        // if (map.isEmpty()) {
        // max = n - 1;
        // }

        // // print map (for debugging)
        // for (Map.Entry<Integer, int[]> e : map.entrySet()) {
        // System.out.println(e.getKey() + " -> " + Arrays.toString(e.getValue())
        // + " sum=" + (e.getValue()[0] + e.getValue()[1]));
        // }

        // System.out.println("Answer = " + max);

        ////////////////////////////////////////////////////////////////////////////////////////////

        // int left = 0; // window start
        // int zeros = 0; // count of zeros in window
        // int maxLen = 0;

        // for (int right = 0; right < arr.length; right++) {
        // if (arr[right] == 0) {
        // zeros++;
        // }

        // // shrink window if more than 1 zero
        // while (zeros > 1) {
        // if (arr[left] == 0) {
        // zeros--;
        // }
        // left++;
        // }

        // // length of window minus one deletion
        // maxLen = Math.max(maxLen, right - left);
        // }

        // System.out.println(maxLen);

        // ///////////////////// Above using 2 stack //////////////////////////////////
        // int arr[] = { 0, 1, 1, 1, 0, 1, 1, 0, 1 };
        int arr[] = { 1, 1, 0, 1 };
        int n = arr.length;

        int left[] = new int[n];
        int right[] = new int[n];
        int count = 0;
        int all1 = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 1) {
                all1++;
                count++;
                left[i] = count;
            } else {
                left[i] = count;
                count = 0;
            }
        }

        ///// for right
        count = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] == 1) {
                count++;
                right[i] = count;
            } else {
                right[i] = count;
                count = 0;
            }
        }

        System.out.println(Arrays.toString(left));
        System.out.println(Arrays.toString(right));
        int max = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) {
                int sum = left[i] + right[i];
                max = Math.max(max, sum);
            }
        }

        System.out.println("Result: " + max);
    }
}
