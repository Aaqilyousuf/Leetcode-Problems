class Solution {
    public String reverseWords(String s) {
        String[] st = s.trim().split("\\s+");
        int l = 0, r = st.length - 1;
        while (l<r){
            String temp = st[l];
            st[l] = st[r];
            st[r] = temp; 
            l++;
            r--;
        }
        return String.join(" ", st);
    }
}