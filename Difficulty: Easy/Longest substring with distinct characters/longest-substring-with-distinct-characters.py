#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        from collections import Counter
        cnt = Counter()
        left, ans = 0, 0
        for r in range(len(s)):
            c = s[r]
            cnt[c] += 1
            while left <= r and cnt[c] > 1:
                lc = s[left]
                cnt[lc] -= 1
                if cnt[lc] == 0:
                    cnt.pop(lc)
                left += 1
            ans = max(ans, len(cnt))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends