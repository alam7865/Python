import java.util.*;

public class subsequence {
    public static void main(String[] args) {
        String str = "12356";

        for (int i = 0; i < str.length(); i++) {
            String str1 = str.substring(0, i);
            String str2 = str.substring(i, str.length());
            System.out.println(str1 + " " + str2);
        }
    }
}