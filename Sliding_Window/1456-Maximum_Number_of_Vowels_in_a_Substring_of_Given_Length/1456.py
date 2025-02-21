class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j = 0, 0
        count, max_count = 0, 0
        vowels = ('a', 'e', 'i', 'o', 'u')

        while j < len(s):
            if s[j] in vowels:
                count += 1
            if j - i + 1 > k:
                if s[i] in vowels:
                    count -= 1
                i += 1
            max_count = max(max_count, count)
            j += 1
        return max_count

if __name__ == '__main__':
    soln = Solution()
    s = "abciiidef"
    k = 3
    print(soln.maxVowels(s, k))