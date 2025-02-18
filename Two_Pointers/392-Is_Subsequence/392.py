class Solution:
    def isSubsequence(self, s, t):
        i, j = 0, 0
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                #print("i: ", i)
                i += 1
            #print("j: ", j)
            j += 1
            #print("Iteration complete")
        if i == len(s):
            return True
        return False
    
if __name__ == '__main__':
    soln = Solution()
    s = "aaaaaa"
    t = "bbaaaa"
    print(soln.isSubsequence(s, t))