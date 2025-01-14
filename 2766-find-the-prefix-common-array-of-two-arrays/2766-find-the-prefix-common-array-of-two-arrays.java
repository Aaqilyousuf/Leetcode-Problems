class Solution {
    private int prefixMatch(int[] A, Set<Integer> setB, int size) {
        int count = 0;
        for (int i = 0; i <= size; ++i) {
            if (setB.contains(A[i])) {
                count++;
            }
        }
        return count;
    }

    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] res = new int[n];
        Set<Integer> setB = new HashSet<>();

        for (int i = 0; i < n; ++i) {
            setB.add(B[i]);
            res[i] = prefixMatch(A, setB, i);
        }

        return res;
    }
}