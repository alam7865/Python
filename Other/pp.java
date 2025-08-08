import java.util.*;

public class pp {
    public static void main(String[] args) {
        String str = "Abc 012..## 10cbA";
        String ss1 = str.toLowerCase();

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < ss1.length(); i++) {
            char ch = ss1.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                sb.append(ch);
            }
        }

        System.out.println(sb.toString());
    }
}