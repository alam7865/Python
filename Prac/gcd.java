import java.util.*;

public class gcd {
    public static void main(String[] args) {
        int n = 5;
        int evenSum = 0;
        int oddSum = 0;
        int c1 = 0;
        int c2 = 0;
        int x1 = 1;
        int x2 = 1;

        while (c1 != n) {
            if (x1 % 2 == 0) {
                evenSum += x1;
                c1++;
            }
            x1++;
        }

        while (c2 != n) {
            if (x2 % 2 != 0) {
                oddSum += x2;
                c2++;
            }
            x2++;
        }

        int a = Math.max(evenSum, oddSum);
        int b = Math.min(evenSum, oddSum);

        while (b != 0) {
            int z = a;
            a = b;
            b = z % b;
        }

        System.out.println("GCD: " + a);
    }
}
