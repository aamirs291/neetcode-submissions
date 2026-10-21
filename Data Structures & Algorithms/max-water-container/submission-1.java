class Solution {
    public int maxArea(int[] heights) {

        int l = 0;
        int r = heights.length-1;
        int max_amt = 0;

        for(int i=0; i<heights.length; i++){
            int area = 0;
            area = (r-l)*Math.min(heights[r],heights[l]);
            max_amt = Math.max(area, max_amt);

            if (heights[l]<heights[r]){
                l+=1;
            }else if(heights[r]<heights[l]){
                r-=1;
            }else {
                l+=1;
            }
        }

        return max_amt;
        
    }
}
