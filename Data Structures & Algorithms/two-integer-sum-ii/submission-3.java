class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int N = numbers.length;
        int l = 0;
        int r = N -1;

        while (l<r){
            int sum = numbers[l]+numbers[r];
            
            if (sum == target){
                return new int[]{l+1, r+1};
            }
            if (sum>target){
                r-=1;
            }
            else{
                l+=1;
            }

        }

        return new int[]{};

        
    }
}
