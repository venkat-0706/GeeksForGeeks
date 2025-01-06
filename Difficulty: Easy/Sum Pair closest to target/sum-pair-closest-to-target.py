#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        n = len(arr)
        arr.sort()
        res = []
        mindiff = float('inf')
        left = 0
        right = n-1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if abs(target - curr_sum) < mindiff:
                mindiff = abs(target -curr_sum)
                res = [arr[left],arr[right]]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return res
        return res
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends