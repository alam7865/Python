import java.util.*;

public class LeetCod {
    public static void main(String args[]) {
        String str = " fPysaRtLQLiMKVvRhMkkDLNedQKffPnCjbITBTOVhoVjiKbfSawvpisDaNzXJctQkn";
        StringBuffer sb = new StringBuffer();
        sb.append('#');

        int n = str.length();

        for (int i = 0; i < n; i++) {
            char ch = str.charAt(i);
            if (ch == '#') {
                continue;
            } else if (ch == ' ') {
                continue;
            } else if (i == 0 || sb.length() == 1) {
                sb.append(Character.toLowerCase(ch));
            } else if (i > 0 && str.charAt(i - 1) == ' ') {
                sb.append(Character.toUpperCase(ch));
            } else {
                sb.append(Character.toLowerCase(ch));
            }

            // Truncate early if length hits 100
            if (sb.length() == 100)
                break;
        }

        // Final check (in case length > 100)
        // if (sb.length() > 100) {
        // return sb.substring(0, 100);
        // }

        System.out.println(sb.toString());
    }
}