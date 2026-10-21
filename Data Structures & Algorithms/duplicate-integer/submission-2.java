class Solution {
    public boolean hasDuplicate(int[] nums) {

        Set<Integer> seen_numbers = new HashSet<>();

        for(int num: nums){

            if(seen_numbers.contains(num)){
                return true;
            }
            seen_numbers.add(num);
            }

    return false;
}

}
