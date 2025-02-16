# Approach 1: Two Pointers - Merge Sort approach 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = len(word1), len(word2)
        p1, p2 = 0, 0 # Initialize two pointers p1 and p2 to loop through word1 and word2
        result = [] # Empty list
        i = 1 # Alternatively loop through word1 and word 2 by setting i = 1 or i = 2
        while p1 < a and p2 < b:
            if i == 1:
                result.append(word1[p1])
                p1 += 1
                i = 2
            else:
                result.append(word2[p2])
                p2 += 1
                i = 1
        # When the index for a and b goes out of bounds then loop through the remaining string individually
        while p1 < a:
            result.append(word1[p1])
            p1 += 1
        while p2 < b:
            result.append(word2[p2])
            p2 += 1
        return ''.join(result)
    
    def mergeAlternatelyString(self, word1: str, word2: str) -> str:
        result = ""
        n1 = len(word1)
        n2 = len(word2)
        for i in range(max(n1, n2)):
            if i < n1:
                result += word1[i]
            if i < n2:
                result += word2[i]
        return result
        

if __name__ == '__main__':
    a = Solution()
    word1 = "abc"
    word2 = "pqr"
    print(a.mergeAlternately(word1, word2))
    print(a.mergeAlternatelyString(word1, word2))