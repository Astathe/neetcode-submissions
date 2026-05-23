class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
    
        char[] c = s.toCharArray();
        char[] c2 = t.toCharArray();

        Arrays.sort(c);
        Arrays.sort(c2);

        for(int i = 0; i < c.length; i++){
            if(c[i] != c2[i]){
                return false;
            }
        }

        return true;
    }
}
