class Solution {
    public boolean isValid(String s) {

        int strLength = s.length();

        Stack<Character> charStack = new Stack<>();
        Set<Character> charSet = new HashSet<>();
        charSet.add(']');
        charSet.add(')');
        charSet.add('}');

        char[] charArray = s.toCharArray();

        for(char charElement: charArray){
            if(charStack.isEmpty() && charSet.contains(charElement)){
                return false;
            }
            if(charSet.contains(charElement)){
                if(charStack.peek()=='(' && charElement==')' || charStack.peek()=='[' && charElement==']' || charStack.peek()=='{' && charElement=='}'){
                    charStack.pop();
                    continue;
                }
                else{
                    return false;
                }
            }
            else{
                charStack.add(charElement);
            }
        }

        return charStack.isEmpty();   
    }
}
