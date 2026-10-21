class Solution {
    public int maxArea(int[] heights) {

        int N = heights.length;
        int l = 0;
        int r = N-1;

        int waterAmount = 0;
        int maxAmount = 0;

        while(l<r){

            waterAmount = (r-l) * Math.min(heights[l], heights[r]);
            maxAmount = Math.max(waterAmount, maxAmount);

            if (heights[l]<= heights[r]){
                l+=1;
            }
            else{
                r-=1;
            }
        }

        return maxAmount;

    }
}