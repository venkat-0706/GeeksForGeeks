class Solution {
  public:
    int largest(vector<int> &arr) {
        // code here
        int num=arr[0];
        int n=arr.size();
        for(int i=1;i<n;i++){
            if(arr[i] > num){
                num=arr[i];
            }
        }
        return num;
    }
};
