package leetcode;

public class ClimbingStairs {
    public int climbStairs(int n) {
        int current = 1;
        int prev = 1;
        int i = 1;
        while (i < n) {
            // loop invariant: current == climbStairs(i) && prev == climbStairs(i-1)
            int tmp = current;
            current = current + prev;
            prev = tmp;
            i++;
        }
        // i == n => current == climbStairs(n)
        return current;
    }
}
