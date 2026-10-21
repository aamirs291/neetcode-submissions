class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for(int num:nums){
            numSet.add(num);
        }
        int longest = 0;
        for(int num:numSet){
            if(!numSet.contains(num-1)){
                int length = 1;
                while (numSet.contains(num+length)){//num+length is the important part here. 
                    length +=1;
                }
                longest = Math.max(longest, length);
            }
        }

        return longest;

    }
}
