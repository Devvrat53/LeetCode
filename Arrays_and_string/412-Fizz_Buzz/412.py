class Solution:
    def fizzBuzz(self, n):
        if n < 1:
            return 1
        
        lst = []
        for i in range(1, n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                lst.append("FizzBuzz")
            elif (i % 3 == 0): 
                lst.append("Fizz")
            elif (i % 5 == 0):
                lst.append("Buzz")
            else:
                lst.append(f"{i}")

        return lst 

if __name__ == '__main__':
    soln = Solution()
    n = 3
    print(soln.fizzBuzz(n))
