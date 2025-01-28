#User function Template for python3

class Solution:
    
    def permute(self, sl, s, i):
        s.add(''.join(sl))
        for j in range(i, len(sl)):
            sl[i], sl[j] = sl[j], sl[i]
            self.permute(sl, s, i+1)
            sl[i], sl[j] = sl[j], sl[i]
    
    def findPermutation(self, s):
        # Code here
        sl = list(s)
        s = set()
        i = 0
        self.permute(sl, s, i)
        return list(s)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends