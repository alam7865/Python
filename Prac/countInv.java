import java.util.Arrays;

public class countInv {

    public static void conquer(int arr[], int si, int mid, int ei) {
        int merged[] = new int[ei - si + 1];
        int idx1 = si;
        int idx2 = mid + 1;
        int x = 0;

        while (idx1 <= mid && idx2 <= ei) {
            if (arr[idx1] <= arr[idx2]) {
                merged[x++] = arr[idx1++];
            } else {
                merged[x++] = arr[idx2++];
            }
        }

        while (idx1 <= mid) {
            merged[x++] = arr[idx1++];
        }

        while (idx2 <= ei) {
            merged[x++] = arr[idx2++];
        }

        for (int i = 0, j = si; i < merged.length; i++, j++) {
            arr[j] = merged[i];
        }
    }

    public static void divide(int arr[], int si, int ei) {
        int count = 0;
        if (si < ei) {
            int mid = si + (ei - si) / 2;
            count += divide(arr, si, mid);
            count += divide(arr, mid + 1, ei);
            count += conquer(arr, si, mid, ei);
        }
        return count;
        // int mid = si + (ei - si) / 2;
        // divide(arr, si, mid);
        // divide(arr, mid + 1, ei);
        // conquer(arr, si, mid, ei);
    }

    public static int mergeSort(int arr[], int si, int ei) {
        return divide(arr, si, ei);
    }

    public static void main(String[] args) {
        int arr[] = { 2, 4, 1, 3, 5 };
        int n = arr.length;

        int si = 0;
        int ei = n - 1;
        int ans = mergeSort(arr, si, ei);
        // int ans = divide(arr, si, ei);

        System.out.println(ans);
    }
}
