class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        int N = nums.length;
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();

        for(int i=0; i<N; i++){
            if(nums[i]>0){
                break;
            }
            if (i>0 && nums[i]==nums[i-1]){
                continue;
            }
            int first = nums[i];
            int targetSum = Math.abs(first);

            int l = i+1;
            int r = N-1;

            while(l<r){
                int sum = nums[l] + nums[r];
                if(sum == targetSum){
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    // res.add(new ArrayList<>(List.of(nums[i],nums[l],nums[r])));
                    l+=1;
                    r-=1;
                    while(l<r && nums[l]==nums[l-1]){
                        l+=1;
                    }
                }
                else if(sum>targetSum){
                    r-=1;
                }
                else{
                    l+=1;
                }
            } 
        }

        return res;
    }
}
