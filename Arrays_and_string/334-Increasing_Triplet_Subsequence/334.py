'''
https://www.youtube.com/watch?v=yEFlGWOVH8g
Time: O(n) Linear Time 
Space: O(1) Constant Space
'''
from math import inf

class Solution:
    def increasingTriplet(self, nums):
        i, j = inf, inf
        n = 0
        while n < len(nums):
            if nums[n] <= i:
                i = nums[n]
            elif nums[n] <= j:
                j = nums[n]
            else:
                return True
            n += 1
        return False
    
    def increasingTriplet1(self, nums):
        first = second = inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    
if __name__ == '__main__':
    soln = Solution()
    nums = [1, 2, 3, 4, 5]
    print(soln.increasingTriplet(nums))