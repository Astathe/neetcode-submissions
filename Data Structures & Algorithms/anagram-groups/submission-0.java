class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> m = new HashMap<>();

        for(String s : strs){
            char[] c = s.toCharArray();
            Arrays.sort(c);
            String a = new String(c);

            m.putIfAbsent(a, new ArrayList<>());
            m.get(a).add(s);
        }

        return new ArrayList<>(m.values());
    }
}
