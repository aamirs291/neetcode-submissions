class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        int N = nums.length;
        List<Integer>[] countFreq = new List[N+1];

        Map<Integer,Integer> freqMap = new HashMap<>();

        for(int i=0; i<N+1; i++){
            countFreq[i] = new ArrayList<>();
        }

        for(int num:nums){
            freqMap.putIfAbsent(num, 0);
            freqMap.put(num, freqMap.get(num) + 1);
        }

        for(Map.Entry<Integer, Integer> entry: freqMap.entrySet()){
            int frequency = entry.getValue();
            int number = entry.getKey();

            countFreq[frequency].add(number);
        }

        int[] res = new int[k];
        int index = 0;
        for(int i=N; i>0; i--){
            for(int num:countFreq[i]){
                res[index] = num;
                index+=1;
                if(index==k){
                    return res;
                }
            }
        }

        return res;

    }
}
