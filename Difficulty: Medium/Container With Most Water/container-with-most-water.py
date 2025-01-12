
class Solution:
    def maxWater(self, a):
        
        n = len(a)
        i, j = 0, n - 1
        ans = 0
        
        while i < j:
            ans = max(ans, min(a[j], a[i]) * (j - i))
            if a[i] < a[j]:
                i += 1
            else:
                j -= 1
        
        return ans

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends