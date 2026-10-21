class Solution {
    public int[] productExceptSelf(int[] nums) {

        int leftProduct = 1;
        int rightProduct = 1;
        int N = nums.length;

        int[] res = new int[N];
        for(int i =0; i<N; i++){
            res[i] = 1;
        }

        for(int i=0; i<N; i++){
            res[i]*=leftProduct;
            leftProduct*=nums[i];
        }

        for(int i=N-1; i>-1; i--){
            res[i]*=rightProduct;
            rightProduct*=nums[i];
        }

        return res;
        
    }
}  
