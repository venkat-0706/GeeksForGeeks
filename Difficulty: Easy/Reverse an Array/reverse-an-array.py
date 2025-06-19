class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        low=0
        high=n-1
        while low< high:
            temp = arr[low]
            arr[low]=arr[high]
            arr[high]= temp
            low+=1
            high-=1

        return arr
        
        
        