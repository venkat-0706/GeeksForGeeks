class Solution {
  public:
    bool isEven(int n) {
        // code here
        if(n&1!=0){
            return false;
        }else{
            return true;
        }
    }
};