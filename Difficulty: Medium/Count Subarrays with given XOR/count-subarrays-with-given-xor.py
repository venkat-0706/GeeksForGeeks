class Solution:
     def subarrayXor(self, arr, k):
        from collections import defaultdict
        prefix_xors = defaultdict(int, {0: 1})
        curr_xor, count = 0, 0
        for a in arr:
            curr_xor ^= a
            count += prefix_xors[curr_xor ^ k]
            prefix_xors[curr_xor] += 1
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends