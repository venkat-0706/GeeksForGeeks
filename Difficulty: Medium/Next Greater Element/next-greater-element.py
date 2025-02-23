# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        res = []
        stack = []
        n = len(arr)
        for i in range(n-1,-1,-1):
            ele = arr[i]
            while stack and stack[-1] <= ele:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(ele)
        return res[::-1]
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends