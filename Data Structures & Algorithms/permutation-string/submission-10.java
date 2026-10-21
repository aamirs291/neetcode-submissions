class Solution {
    public boolean checkInclusion(String s1, String s2) {

        int N = s1.length();
        int M = s2.length();

        if (M<N){
            return false;
        }

        int k = N;

        Map<Character, Integer> s1CharMap = new HashMap<>();
        Map<Character, Integer> s2CharMap = new HashMap<>();

        for(int i=0; i<N; i++){
            char currChar = s1.charAt(i);
            s1CharMap.put(currChar, s1CharMap.getOrDefault(currChar, 0) + 1);

            char s2CurrChar = s2.charAt(i);
            s2CharMap.put(s2CurrChar, s2CharMap.getOrDefault(s2CurrChar, 0) + 1); 
        }

        if (s1CharMap.equals(s2CharMap)){
            return true;
        }

        for(int l=1; l<M-k+1; l++){
            char prevChar = s2.charAt(l-1);
            s2CharMap.put(prevChar, s2CharMap.get(prevChar)-1);
            if(s2CharMap.get(prevChar)==0){
                s2CharMap.remove(prevChar);
            }

            char addChar = s2.charAt(k+l-1);
            s2CharMap.put(addChar, s2CharMap.getOrDefault(addChar, 0)+1);

            if(s1CharMap.equals(s2CharMap)){
                return true;
            }
        }

        return false;


        
    }
}
