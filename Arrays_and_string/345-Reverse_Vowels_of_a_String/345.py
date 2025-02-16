class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lst = list(s)
        i, j = 0, len(lst)-1
        temp = 0
        
        while i < len(lst) and j > i:
            if lst[i] in vowels and lst[j] in vowels:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            else:
                if lst[i] in vowels:
                    j -= 1
                elif lst[j] in vowels:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return "".join(lst)
            
if __name__ == '__main__':
    soln = Solution()
    s = "IceCreAm"
    print(soln.reverseVowels(s))
