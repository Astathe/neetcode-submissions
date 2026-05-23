class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        length = len(arr)
        count = 1
        temp = 1
        l = 0
        r = 1
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            if arr[0] != arr[1]:
                return 2
            else:
                return 1
        while l in range(length - 1):
            for i in range(l, r):
                if r == length:
                    l = length
                    break
                if arr[i] == arr[r]:
                    l += 1
                    r = l + 1
                    if count < temp:
                        count = temp
                    temp = 1                    
                    break
                if i == (r - 1):
                    i = l
                    r += 1
                    temp += 1
        if count > temp:
            return count
        else: 
            return temp

                    