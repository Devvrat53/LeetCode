class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        boleanlst = []
        for i in range(len(candies)):
            surpluscandies = candies[i] + extraCandies

            if surpluscandies >= max(candies):
                boleanlst.append('true')
            else:
                boleanlst.append('false')
        return boleanlst

if __name__ == '__main__':
    soln = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    lst = soln.kidsWithCandies(candies, extraCandies)
    print(lst)