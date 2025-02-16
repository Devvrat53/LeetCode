class Solution:
    # Euclidian Approach 
    def get_gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a%b # Euclidian algorithm
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        # Return the common prefix of length gcd_length
        gcd_length = self.get_gcd(len(str1), len(str2))
        return str1[:gcd_length]
    
    # Recursive Euclidian Approach
    def get_gcd_recursive(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.get_gcd_recursive(b, a%b)
    
    def gcd_of_strings_recursive(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = self.get_gcd_recursive(len(str1), len(str2))

        return str1[:gcd_length]
    
if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))