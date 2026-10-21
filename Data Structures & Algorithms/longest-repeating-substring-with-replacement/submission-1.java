class Solution {
    public int characterReplacement(String s, int k) {

        int N = s.length();
        Map<Character, Integer> charFreq = new HashMap<>(); 
        // repeating + n_repeating = total_length
        int l = 0;
        int res = 0;

        int currMaxFreq = 0;

        for(int r=0; r<N; r++){
            char currentChar = s.charAt(r);
            charFreq.put(currentChar, charFreq.getOrDefault(currentChar, 0) + 1);
            
            currMaxFreq = Math.max(currMaxFreq, charFreq.get(currentChar));

            while (((r-l+1) - currMaxFreq) > k){
                charFreq.put(s.charAt(l), charFreq.get(s.charAt(l))-1);
                l+=1;
            }

            res = Math.max(res, r-l+1);
            
        }
        
        return res;
    }
}
