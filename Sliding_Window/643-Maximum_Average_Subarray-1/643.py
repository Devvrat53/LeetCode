class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_avg = window_sum/k
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_avg = max(max_avg, window_sum/k)
        return max_avg

if __name__ == '__main__':
    soln = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(soln.findMaxAverage(nums, k))