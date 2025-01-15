# User function Template for python3

class Solution:
     def longestSubarray(self, arr, k):  
        # code here
        
        m = {0: -1}
        s, ans = 0, 0
        for i, e in enumerate(arr):
            s += arr[i]
            if s-k in m:
                ans = max(ans, i - m[s-k])
            if s not in m:
                m[s] = i
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends