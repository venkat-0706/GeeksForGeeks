class Solution {
  public:
    bool checkKthBit(int n, int k) {
        // Your code here
        if((n&(1<<k))>0){
            return true;
        } else{
            return false;
        }
    }
};