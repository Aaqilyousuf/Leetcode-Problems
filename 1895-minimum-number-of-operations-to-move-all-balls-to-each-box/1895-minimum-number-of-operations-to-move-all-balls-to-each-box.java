class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int sum = 0;
        int rightOnes = 0;
        
        // Calculate initial sum and count of '1's to the right
        for (int i = 0; i < n; ++i) {
            if (boxes.charAt(i) == '1') {
                sum += i;
                rightOnes++;
            }
        }
        
        // Calculate moves per position
        int[] res = new int[n];
        int prefixSum = 0;
        int leftOnes = 0;
        
        for (int i = 0; i < n; ++i) {
            int moves = sum + prefixSum;
            res[i] = moves;
            
            // Update both sum and prefixSum
            if (boxes.charAt(i) == '1') {
                leftOnes++;
                rightOnes--;
            }
            prefixSum += leftOnes;
            sum -= rightOnes;
        }
        
        return res;
    }
}