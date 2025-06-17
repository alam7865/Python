import java.util.*;

public class tower {
    public static int calculateCost(int heights[], int cost[], int target) {
        int totalCost = 0;

        for (int i = 0; i < heights.length; i++) {
            totalCost += Math.abs(heights[i] - target) * cost[i];
        }

        return totalCost;
    }

    public static void main(String args[]) {
        int heights[] = { 6, 1, 100 };
        int cost[] = { 1000, 2, 10 };
        int ans = Integer.MAX_VALUE;

        int low = 100000 + 9;
        int high = 0;

        for (int i : heights) {
            low = Math.min(low, i);
            high = Math.max(high, i);
        }

        while (low <= high) {
            int mid = (low + high) / 2;

            int midcost = calculateCost(heights, cost, mid);
            int midcostPlus1 = calculateCost(heights, cost, mid + 1);

            ans = Math.min(midcost, midcostPlus1);

            if (midcost < midcostPlus1) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        System.out.println("Result: " + ans);
    }
}