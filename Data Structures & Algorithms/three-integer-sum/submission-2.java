class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int i = 0;
        while(i<nums.length){
        // for(int i=0; i<nums.length; i++){
            if (nums[i]>0) break;
            if (i>0 && nums[i]==nums[i-1]){
                i++;
                continue;
            }
            //int currSum = nums[i];
            int target = Math.abs(nums[i]);
            int l = i+1;
            int r = nums.length - 1;
            while(l<r){
                int currSum = nums[l] + nums[r];
                if (currSum > target){
                    r--;
                }else if (currSum < target){
                    l++;
                }else{
                    res.add(new ArrayList<>(List.of(nums[i],nums[l],nums[r])));
                    l++;
                    r--;
                    while (l<r && nums[l]==nums[l-1]){
                        l++;
                    }
                }
            }
        i++;
        }
        // System.out.println(res);
        return res;
    }
}
