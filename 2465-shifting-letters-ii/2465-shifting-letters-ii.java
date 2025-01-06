class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        //in this program we used difference array technique
        int n = s.length();
        int[] arr = new int[n+1]; //increase the size by becasue for handle edge case
        for (int[] shift : shifts) {
            if (shift[2] == 1) { //fw
                arr[shift[0]]++;
                arr[shift[1] + 1]--;
                
            } else { //bw
                arr[shift[0]]--;
                arr[shift[1] + 1]++;
            }
        }
        //compute prefix sum actuall shifts
        for(int i=1;i<=n;i++){
            arr[i] += arr[i-1];
        }

        StringBuilder result = new StringBuilder(s);
        for (int i = 0; i < n; i++) {
            int count = arr[i] % 26;
            if(count<0){
                count += 26;
            }
            char cur = (char) (((s.charAt(i)) - 'a' + count) % 26 + 'a');
            result.setCharAt(i, cur);
        }
        return result.toString();
    }
}