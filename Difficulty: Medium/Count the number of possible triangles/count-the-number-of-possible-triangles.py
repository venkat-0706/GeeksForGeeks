#User function Template for python3

class Solution:
      def countTriangles(self, arr):
        # code here
        from bisect import bisect_left
        arr.sort()
        ans, n = 0, len(arr)
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i] + arr[j]
                k = bisect_left(arr, s, j+1)
                ans += k-j-1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends