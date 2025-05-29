#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        arr.sort()
        count=0
        for i in range(len(arr)):
            if(arr[i]==0):
                count+=1
        return count
        # code here