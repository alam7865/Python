import java.util.*;

public class ksubstring {
    public static int atMostKsubstring(String str, int n, int k) {
        HashMap<Character, Integer> map = new HashMap<>();
        int start = 0;
        int count = 0;
        for (int end = 0; end < n; end++) {
            char ch = str.charAt(end);
            map.put(ch, map.getOrDefault(ch, 0) + 1);

            while (map.size() > k) {
                char ch2 = str.charAt(start);
                map.put(ch2, map.get(ch2) - 1);
                if (map.get(ch2) == 0) {
                    map.remove(ch2);
                }
            }

            count += end - start + 1;
        }

        return count;
    }

    public static void main(String[] args) {
        String str = "aa";
        int k = 1;
        int ans = atMostKsubstring(str, str.length(), k);
        System.out.println("Result: " + ans);
    }
}
