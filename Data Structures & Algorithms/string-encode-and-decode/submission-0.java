class Solution {

    public String encode(List<String> strs) {

        StringBuilder res = new StringBuilder();
        for(String str: strs){
            res.append(str.length()).append('#').append(str);
        }

        return res.toString();

    }

    public List<String> decode(String str) {

        List<String> res = new ArrayList<>();
        int i = 0;
        while(i<str.length()){
            int j = i;
            while(str.charAt(j)!='#'){
                j++;
            }

            int length = Integer.parseInt(str.substring(i,j));
            // i and j above is to extract the length part from the encoded format
            i = j + 1; // j would have exited when it reached # so i would be the start of the string
            j = i + length; // j here would land on the length part of the next string
            res.add(str.substring(i,j));
            i = j;//i is being marked to begin at the length part of the string. this is necesarry to reset the pointers to be able to reuse the while loop above.
            // i and j here is to set the pointers for every subseq strings in the encoded format
        }

        return res;

    }
}
