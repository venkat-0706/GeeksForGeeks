#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def getMaxArea(self,arr):
        #code here
        left = [1]*len(arr)
        right = [1]*len(arr)
        
        for i in range(1, len(arr)):
            ic = i - 1
            while ic >= 0 and arr[i] <= arr[ic]:
                left[i] += left[ic]
                ic -= left[ic]
                
        for i in range(len(arr)-2, -1, -1):
            ic = i + 1
            while ic < len(arr) and arr[i] <= arr[ic]:
                right[i] += right[ic] 
                ic += right[ic]
                
        maxi = -1
        
        for i in range(len(arr)):
            t = (left[i] + right[i] - 1) * arr[i]
            maxi = max(maxi, t)
            
        return maxi

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends