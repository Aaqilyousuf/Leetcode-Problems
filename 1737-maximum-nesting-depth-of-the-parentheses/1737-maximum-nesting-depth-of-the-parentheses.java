class Solution {
    public int maxDepth(String s) {
        int maxCount = -1;
        int cnt = 0;
        s.toCharArray();
        for (char c: s.toCharArray()){
            if(c == '('){
                cnt++;
            }else if(c == ')'){
                cnt--;
            }
            maxCount = Math.max(maxCount, cnt);;
        }
        return maxCount;
    }
}