class Solution {
  public:
    int largest(vector<int> &arr) {
        // code here
        int n=arr.size();
        int res=arr[0];
        for(int i=1;i<n;i++){
            if(arr[i] > res){
                res=arr[i];
            }
        }
        return res;
    }
};
