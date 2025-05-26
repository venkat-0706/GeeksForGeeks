class Solution {
  public:
    int setBits(int n) {
        // Write Your Code here
        int res = 0;
        while(n>0){
            if(n&1!=0){
                res++;
            }
            n=n/2;
        }
        return res;
    }
};