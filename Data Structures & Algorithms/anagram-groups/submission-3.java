class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        int N = strs.length;

        HashMap<String, List<String>> wordFreq = new HashMap<>();

        for(String str:strs){
            char[] charFreq = new char[26];
            for(char ch: str.toCharArray()){
                int charIdx = ch - 'a';
                charFreq[charIdx] += 1;
            }
            String charKey = String.valueOf(charFreq);
            
            List<String> wordList = wordFreq.getOrDefault(charKey, new ArrayList<>());
            wordList.add(str);
            wordFreq.put(charKey, wordList);
        }

        return new ArrayList<>(wordFreq.values());


    }
}
