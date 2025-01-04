import java.util.stream.LongStream;
class Solution {
    public int waysToSplitArray(int[] nums) {
        long tot = 0;
        for(int val: nums){
            tot += val;
        }
        long prefix = 0;
        int cnt = 0;
        for(int i=0;i<nums.length-1;i++){
            prefix += nums[i];
            long suffix = tot - prefix;
            if (prefix >= suffix){
                cnt++;
            }
        }
        return cnt;
    }
}