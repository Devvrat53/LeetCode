class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed2 = [0] + flowerbed + [0] # Adding 2 zeroes at start and end

        for i in range(1, len(flowerbed2)-1):
            if flowerbed2[i-1] == 0 and flowerbed2[i] == 0 and flowerbed2[i+1] == 0:
                flowerbed2[i] = 1
                n -= 1
        return n <= 0
    
if __name__ == '__main__':
    soln = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(soln.canPlaceFlowers(flowerbed, n))