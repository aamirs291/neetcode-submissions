class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> pairMap = new HashMap<>();

        for(int i = 0; i<nums.length; i++){
            int diff = target - nums[i];
            if (pairMap.containsKey(diff)){
                return new int[]{pairMap.get(diff), i};
            }
            pairMap.put(nums[i], i);
        }

        return new int[]{};
    }
}
