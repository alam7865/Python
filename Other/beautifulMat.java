import java.util.*;

public class beautifulMat {
    public static void main(String args[]) {
        int mat[][] = { { 1, 2 }, { 3, 4 } };
        int n = mat.length;
        int m = mat[0].length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(mat[j][i] + " ");
            }
            System.out.println();
        }
    }
}