import java.util.*;

public class pp1 {
    public static void main(String[] args) {
        // String s = "aaaaaa";
        // StringBuilder sb = new StringBuilder();
        // int n = s.length();

        // if (n == 1) {
        // sb.append(s.charAt(0));
        // // return sb.toString();
        // }

        // int j = 0;
        // int count = 1;

        // for (int i = 1; i < n; i++) {
        // if (s.charAt(i) != s.charAt(j)) {
        // while (count-- > 0) {
        // sb.append(s.charAt(j));
        // }

        // count = 1;
        // j = i;
        // }

        // else if ((s.charAt(i) == s.charAt(j)) && count < 2) {
        // count++;
        // }

        // }

        // if (s.charAt(n - 1) != s.charAt(n - 2)) {
        // sb.append(s.charAt(n - 1));
        // } else {
        // sb.append(s.charAt(n - 1));
        // sb.append(s.charAt(n - 1));
        // }

        // // return sb.toString();
        // System.out.println(sb.toString());
        //////////////////////////////////////////////////////////////////////////////

        String s = "aeiou";
        HashMap<Character, Integer> map = new HashMap<>();

        int n = s.length();

        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);

            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        int dublic = 1;

        // System.out.println(map.toString());
        for (Map.Entry<Character, Integer> set : map.entrySet()) {
            int val = set.getValue();
            dublic = dublic * val;
        }

        // System.out.println(dublic);
        int count = map.size();

        for (int i = count; i >= 1; i--) {
            dublic = dublic * i;
        }

        System.out.println(dublic);
        // return dublic;

    }
}