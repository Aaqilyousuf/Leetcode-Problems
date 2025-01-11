class Solution {
    public int beautySum(String s) {
        int res = 0;
        for(int i=0;i<s.length(); i++){
            int[] alpha = new int[26];
            for(int j=i;j < s.length(); j++){
                alpha[s.charAt(j) - 'a']++;
                res += beauty(alpha);
            }
        }
        return res;
    }
    public int beauty(int[] alpha){
        int mf = -1;
        int lf = Integer.MAX_VALUE;
        for(int i=0;i<alpha.length; i++){
            mf = Math.max(mf, alpha[i]);
            if(alpha[i]>=1){
                lf = Math.min(lf, alpha[i]);
            }
        }
        return mf-lf;
    }
}