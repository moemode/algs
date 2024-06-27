package leetcode;

public class HouseRobber {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return -1;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int prev = nums[0];
        int current = Math.max(prev, nums[1]);
        int tmp;
        for (int i = 2; i < nums.length; i++) {
            tmp = current;
            current = Math.max(prev + nums[i], current);
            prev = tmp;
        }
        return current;
    }

}
