import java.util.*;

public class dsa {
    public static void main(String[] args) {
        // int arr[] = { 16, 17, 4, 3, 5, 2 };
        // int n = arr.length;
        // int res[] = new int[n];

        // Stack<Integer> st = new Stack<>();

        // for (int i = n - 1; i >= 0; i--) {
        // // is stack empty or
        // int pres = arr[i];
        // if (st.isEmpty()) {
        // res[i] = -1;
        // } else {
        // res[i] = st.peek();
        // }

        // // if arr[i]>greater then present
        // while (!st.isEmpty() && arr[i] >= st.peek()) {
        // st.pop();
        // }

        // if (st.isEmpty() || arr[i] > st.peek()) {
        // if (st.isEmpty()) {
        // res[i] = -1;
        // } else {
        // res[i] = st.peek();
        // }
        // }

        // st.push(pres);
        // }

        // System.out.println(Arrays.toString(res));

        // /////////////////////////////// Just next greater element
        // ////////////////////////////

        int arr[] = { 16, 17, 4, 3, 5, 2 };

        Stack<Integer> st = new Stack<>();
        st.push(-1);
        int n = arr.length;
        int res[] = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int pres = arr[i];
            if (arr[i] > st.peek()) {
                while (!st.isEmpty() && arr[i] >= st.peek()) {
                    // pop
                    st.pop();
                }
            }

            if (st.isEmpty()) {
                arr[i] = -1;
            } else {
                arr[i] = st.peek();
            }

            st.push(pres);
        }

        System.out.println(Arrays.toString(arr));
    }
}
