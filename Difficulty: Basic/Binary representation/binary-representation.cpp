class Solution {
  public:
    string getBinaryRep(int n) {
        // Write Your Code here
        string ans = " ";
        for(int i=31;i>=0;i--){
            if(n&(1<<i)){
                ans+='1';
            } else{
                ans += '0';
            }
        }
        return ans;
    }
};