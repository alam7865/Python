import java.util.*;

public class tywinWar {
    public static void main(String args[]) {
        int arr[] = { 5, 6, 3, 2, 1 };
        int k = 2;
        int n = arr.length;
        int mid = n / 2;
        if (n % 2 != 0) {
            mid++;
        }
        System.out.println(mid);
        int divisible = 0;

        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            int num = arr[i];
            if (num % k != 0) {
                list.add(num % k);
            }

            if (arr[i] % k == 0) {
                divisible++;
            }
        }

        if (divisible >= mid) {
            System.out.println("Yes Found");
        }

        Collections.sort(list);

        int count = 0;
        int low = 0;
        while (low < list.size() && divisible < mid) {
            count += list.get(low);
            divisible++;
            low++;
        }

        System.out.println("Found: " + count);
    }
}