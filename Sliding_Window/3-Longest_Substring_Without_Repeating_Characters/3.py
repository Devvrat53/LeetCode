class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        i, j = 0, 0
        max_length = 0
        sett = set()

        while j < len(s):
            while s[j] in sett: # when duplicate element is found and window is invalid remove from set
                sett.remove(s[i]) 
                i += 1
            sett.add(s[j])
            if (max_length < j-i+1): # j-i+1 = size of the window
                max_length = j-i+1
            j += 1
        return max_length

if __name__ == '__main__':
    s = "abcabcbb"
    soln = Solution()
    print(soln.lengthOfLongestSubstring(s))