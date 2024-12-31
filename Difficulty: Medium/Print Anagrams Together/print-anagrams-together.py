#User function Template for python3

from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        n = len(arr)
        res = []
        mp = {}
        for i in range(n):
            s =  arr[i]
            s = ''.join(sorted(s))
            if s not in mp:
                mp[s] = len(res)
                res.append([])
            res[mp[s]].append(arr[i])
        return res
            

        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends