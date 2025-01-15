class Solution:
    def maxLen(self, arr):
        max_len = 0
        cumsum = 0
        hashmap = {0: -1}  # Initialize hashmap with cumsum 0 at index -1

        for i in range(len(arr)):
            # Increment or decrement cumsum based on the value
            cumsum += 1 if arr[i] == 1 else -1

            if cumsum in hashmap:
                # If the cumsum has been seen before, calculate the subarray length
                max_len = max(max_len, i - hashmap[cumsum])
            else:
                # Store the first occurrence of this cumsum
                hashmap[cumsum] = i

        return max_len


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends