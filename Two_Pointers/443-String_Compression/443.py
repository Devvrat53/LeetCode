'''
Time : O(n) Linear Time (Use of single loop)
Space: O(1) Constant Space (No array/sets/hashmaps used)
'''
class Solution:
    def compress(self, chars):
        i, j = 0, 0

        while i < len(chars):
            ch = chars[i]
            count = 0
            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1
            
            chars[j] = ch
            j += 1
            if count > 1:
                for k in range(len(str(count))):
                    chars[j] = str(count)[k]
                    j += 1
        return j 
    
if __name__ == '__main__':
    soln = Solution()
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(soln.compress(chars))
