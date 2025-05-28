class Solution {
  public:
    int binarysearch(vector<int> &arr, int k) {
        // code here
        int n=arr.size();
        int low=0, high=n-1, res =-1;
        while(low<=high){
            int mid = (low+high)/2;
            if(arr[mid]== k){
                res =mid;
                high=mid-1;
            } else if(arr[mid] < k){
                low = mid+1;
            } else{
                high = mid-1;
            }
        }
        return  res;
    }
};