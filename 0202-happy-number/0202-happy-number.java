import java.util.HashSet;

class Solution {
    public boolean isHappy(int n) {
        if (n == 1 || n == 7) return true;
        if (n % 10 == n) return false;

        HashSet<Integer> seen = new HashSet<>();
        while (n != 1 && !seen.contains(n)) {
            seen.add(n);
            int sum = 0;
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            n = sum;
        }
        return n == 1;
    }
}
