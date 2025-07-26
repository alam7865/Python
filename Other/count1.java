import java.util.*;

public class count1 {

    public static int solve(int num, int target, int count) {
        if (num == target) {
            return count;
        }

        if (num > target) {
            return -1;
        }
        int cc = count;
        int multiply2 = solve(num * 2, target, cc + 1);
        int multiply3 = solve(num * 3, target, cc + 1);

        if (multiply2 != -1) {
            return multiply2;
        }

        if (multiply3 != -1) {
            return multiply3;
        }

        return -1;
    }

    public static void main(String[] args) {
        // int num = 21;
        // int target = 56;
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int target = sc.nextInt();

        int ans = solve(num, target, 0);

        System.out.println(ans);
    }
}