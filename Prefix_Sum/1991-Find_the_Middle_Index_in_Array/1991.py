class Solution:
    def findMiddleIndex(self, nums):
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

if __name__ == '__main__':
    soln = Solution()
    nums = [2, 3, -1, 8, 4]
    print(soln.findMiddleIndex(nums))
