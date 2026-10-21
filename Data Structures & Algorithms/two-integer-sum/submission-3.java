class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> indices_list = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            int diff = target-nums[i];
            if(indices_list.containsKey(diff)){
                return new int[] { indices_list.get(diff),i };
            }
            indices_list.put(nums[i], i);
        }

        return new int[] {};
        
    }
}
