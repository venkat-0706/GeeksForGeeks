#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        temp = list(set(arr))
        temp.sort()
        if len(temp) > 1:
            return temp[-2]
        return -1
        # Code Here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends