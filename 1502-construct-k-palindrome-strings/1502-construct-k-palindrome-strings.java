class Solution {
    public boolean canConstruct(String s, int k) {
        if(s.length() < k){
            return false;
        }
        int n = s.length();
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i=0;i<n;i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0)+1);
        }
        int cntOdd = 0;
        for (int freq : map.values()) {
            if (freq % 2 != 0) {
                cntOdd++;
            }
        }
        return cntOdd <= k;
    }
}