class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> freqMap = new HashMap<>();
        
        for(String str: strs){
            int[] freqArray = new int[26];
            for(char ch: str.toCharArray()){
                freqArray[ch-'a']+=1;
            }

            String key = Arrays.toString(freqArray);
            freqMap.putIfAbsent(key, new ArrayList<>());
            freqMap.get(key).add(str);
        }

        return new ArrayList<>(freqMap.values());
    }
}
