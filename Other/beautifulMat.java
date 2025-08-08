import java.util.*;

public class beautifulMat {
    public static void main(String args[]) {
        // int mat[][] = { { 1, 2 }, { 3, 4 } };
        // int n = mat.length;
        // int m = mat[0].length;

        // for (int i = 0; i < n; i++) {
        // for (int j = 0; j < m; j++) {
        // System.out.print(mat[j][i] + " ");
        // }
        // System.out.println();
        // }

        String s = "IX";
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int sum = map.get(s.charAt(0));

        for (int i = 1; i < s.length(); i++) {
            if (map.get(s.charAt(i - 1)) >= map.get(s.charAt(i))) {
                sum += map.get(s.charAt(i));
            } else {
                sum -= map.get(s.charAt(i));
            }

            // System.out.println(s.charAt(i));
            // System.out.println("Sum: " + sum);
        }

        System.out.println(Math.abs(sum));
    }
}