class Solution:
    def binarysearch(self, arr, k):
        temp = set(arr)
        n=len(arr)
        for i in range(n):
            if k in temp:
                return arr.index(k)
        return -1
        
        # Code Here