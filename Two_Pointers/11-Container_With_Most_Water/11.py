'''
Time: O(n) Only 1 loop
Space: O(1) No ds used
'''
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height)-1
        result = 0
        while i < j:
            min_height = min(height[i], height[j])
            result = max(result, min_height * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result
    
    def maxArea1(self, height):
        i, j = 0, len(height)-1
        result = 0
        while i < j:
            area = (j-i) * min(height[i], height[j]) # Area of rectangle
            result = max(result, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result

if __name__ == '__main__':
    soln = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(soln.maxArea(height))