# User function Template for python3
class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        n,curr=len(arr),0
        right=[0]*n
        
        for i in range(n-1,-1,-1):
            curr+=arr[i]
            right[i]=curr
            
        curr=arr[0]
        for i in range(1,n-1):
            if curr==right[i+1]:
                return i
            curr+=arr[i]
            
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends