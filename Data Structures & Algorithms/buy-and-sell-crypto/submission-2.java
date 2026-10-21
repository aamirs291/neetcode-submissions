class Solution {
    public int maxProfit(int[] prices) {

        int N = prices.length;
        int profit = 0;
        int maxprofit = 0;
        int currLow = prices[0];

        for(int i = 0; i<N; i++){
            if (prices[i]<currLow){
                currLow = prices[i];
            }
            profit = prices[i] - currLow;
            maxprofit = Math.max(profit, maxprofit);
        }

        return maxprofit;
        
    }
}
