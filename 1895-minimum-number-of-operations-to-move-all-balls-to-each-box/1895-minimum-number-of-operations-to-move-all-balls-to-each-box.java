class Solution {
    public int[] minOperations(String boxes) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<boxes.length(); i++){
            if(boxes.charAt(i)=='1'){
                list.add(i);
            }
        }
        int [] arr = new int[boxes.length()];
        for(int i=0; i<boxes.length(); i++){
            int sum =0;
            for(int num : list){
                sum += Math.abs(i-num);
            }
            arr[i] = sum;
        }
        return arr;
    }
}