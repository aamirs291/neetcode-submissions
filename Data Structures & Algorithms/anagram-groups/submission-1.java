class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        for(String s: strs){
            int[] countFreq = new int[26];
            for(char c: s.toCharArray()){
                countFreq[c-'a']+=1;
            }
            //convert the countFreq array to be a string
            String key = Arrays.toString(countFreq);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }

        return new ArrayList<>(res.values());
    }
}
