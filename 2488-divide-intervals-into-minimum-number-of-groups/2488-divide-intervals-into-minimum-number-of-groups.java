class Solution {
    public int minGroups(int[][] intervals) {
        int length = intervals.length;
        List<int[]> events = new ArrayList<>();

        for (int i=0; i<length; ++i){
            events.add(new int[] {intervals[i][0], 1});
            events.add(new int[] {intervals[i][1]+1, -1});
        }
        events.sort((a, b)-> a[0]==b[0]? a[1]-b[1] : a[0]-b[0]);
        int maxOverlap = 0;
        int overlap = 0;
        for (int[] event: events){
            overlap += event[1];
            maxOverlap = Math.max(maxOverlap, overlap);
        }
        return maxOverlap;
    }
}