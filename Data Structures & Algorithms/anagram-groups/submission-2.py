class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_list = [[strs[0]]]

        for i in range (1, len(strs)):
            word1 = list(strs[i])
            word1.sort()
            t = True
            for k in range(len(my_list)):
                word2 = list(my_list[k][0])
                word2.sort()
                if word1 == word2:
                    my_list[k].append(strs[i])
                    t = False
            if t == True:
                my_list.append([strs[i]])
        return my_list