
class Solution:
    def countTriplets(self, arr, target):
        from collections import defaultdict
        m = defaultdict(int)
        for e in arr:
            m[e] += 1
        
        ans = 0
        for i in range(len(arr)):
            m[arr[i]] -= 1             #remove the current element
            for j in range(0, i):     #traverse from 0 until to i(not included) because these element have been removed by the above line during their turn
                lookfor = target-arr[i]-arr[j]
                ans += m[lookfor]
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends