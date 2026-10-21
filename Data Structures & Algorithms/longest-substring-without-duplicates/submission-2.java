class Solution {
    public int lengthOfLongestSubstring(String s) {

        int N = s.length();

        Map<Character, Integer> charMap = new HashMap<>();
        int l = 0;
        //int r = N -1;
        int maxLength = 0;

        for(int r = 0; r<N; r++){
            Character ch = s.charAt(r);
            charMap.put(ch, charMap.getOrDefault(ch, 0) + 1);

            while(l<r && charMap.get(ch) > 1){
                Character leftChar = s.charAt(l);
                charMap.put(leftChar, charMap.get(leftChar) - 1);
                l++;
            }

            maxLength = Math.max(maxLength, r-l+1);
            // maxLength = r-l+1;
        }

        return maxLength;

        
    }
}
