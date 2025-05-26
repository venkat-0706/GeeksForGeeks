// User function Template for C++

class Solution {
  public:
    // Function to check if given number n is a power of two.
    bool isPowerofTwo(int n) {
        // code here
        if(n==1){
            return true;
        }
        while(n!=1){
            if(n&1 !=0){
                return false;
            }
            n=n/2;
        }
        return true;
    }
};