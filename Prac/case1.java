import java.util.*;

public class case1 {
    public static void main(String args[]) {
        // ArrayList<Character> list1 = new ArrayList<>();

        // list1.add('B');
        // list1.add('A');
        // Collections.sort(list1);
        // System.out.println(list1.toString());

        int arr[] = { 4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11 };
        int k = 14;
        Arrays.sort(arr);

        int n = arr.length;

        for (int i = 0; i < n; i += 3) {
            int last = i + 2;
            if (arr[last] - arr[i] <= k) {
                System.out.println(arr[i] + " " + arr[i + 2] + " " + arr[last]);
            }
        }
    }
}