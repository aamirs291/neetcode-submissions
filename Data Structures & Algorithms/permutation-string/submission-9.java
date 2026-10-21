class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character, Integer> s1charMap = new HashMap<>();
        Map<Character, Integer> s2charMap = new HashMap<>();

        int k = s1.length();
        int N = k;
        int M = s2.length();

        if (M<k) return false;

        for(int i=0; i<N; i++){
            Character ch = s1.charAt(i);
            s1charMap.put(ch, s1charMap.getOrDefault(ch, 0)+ 1);
        }

        for(int j=0; j<k; j++){
            Character ch = s2.charAt(j);
            s2charMap.put(ch, s2charMap.getOrDefault(ch, 0)+ 1);
        }

        if(s1charMap.equals(s2charMap)) return true;

        for(int j=1; j<M-k+1; j++){
            Character charToRemove = s2.charAt(j-1);
            Character charToAdd = s2.charAt(k+j-1);

            s2charMap.put(charToRemove, s2charMap.get(charToRemove)-1);
            if (s2charMap.get(charToRemove) == 0) s2charMap.remove(charToRemove);

            s2charMap.put(charToAdd, s2charMap.getOrDefault(charToAdd, 0) + 1);

            if (s1charMap.equals(s2charMap)) return true;
        }

    return false;
    }
}
