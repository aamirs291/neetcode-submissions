class Solution {
    public int lengthOfLongestSubstring(String s) {

        int N = s.length();
        int currLength = 0;
        int maxLength = 0;

        int l = 0;
        Map<Character, Integer> charFreq = new HashMap<>();

        for(int r=0; r<N;r++){
            char currChar = s.charAt(r);
            charFreq.put(currChar, charFreq.getOrDefault(currChar, 0) + 1);

            while (l<r && charFreq.get(currChar)>1){
                charFreq.put(s.charAt(l), charFreq.get(s.charAt(l))-1);
                l+=1;
            }

            currLength = r-l+1;
            maxLength = Math.max(currLength, maxLength);
        }

        return maxLength;
        
    }
}
