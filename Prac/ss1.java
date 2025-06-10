import java.util.*;

public class ss1 {
    public static void main(String[] args) {
        String s = "geek";

        int arr[] = new int[26];
        int n = s.length();

        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            int idx = ch - 'a';
            arr[idx]++;
        }

        int ans = 0;
        int count = 0;

        for (int i = 0; i < 26; i++) {
            int val = arr[i];
            if (val > 0) {
                ans += (n - val);
            }

            if (val > 1) {
                count += val;
            }
        }

        ans = ans / 2;

        ans = ans + count;

        System.out.println(ans);
    }
}