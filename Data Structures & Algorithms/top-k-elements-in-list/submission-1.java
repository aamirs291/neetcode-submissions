class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> countFreq = new HashMap<>();
        List<Integer>[] freqArray = new List[nums.length+1];

        for(int i=0;i<nums.length+1; i++){
            freqArray[i] = new ArrayList<>();
        }

        for(int num:nums){
            countFreq.put(num, countFreq.getOrDefault(num, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry: countFreq.entrySet()){
            freqArray[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;

        // for(List list: freqArray){
        //     System.out.print(list);
        // }
        // System.out.print(countFreq);

        for(int i=nums.length; i>0 && index<k; i--){
            for(int num: freqArray[i]){
                res[index++] = num;
            }   
        }

        return res;

    }
}
