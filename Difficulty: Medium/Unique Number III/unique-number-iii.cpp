// User function Template for C++

class Solution {
  public:
    int getSingle(vector<int> &arr) {
        // code here
        sort(arr.begin(),arr.end());
        int n=arr.size();
        int count=0;
        for(int i=0;i<n;i++){
            if(arr[i]!= arr[i+1] &&  arr[i]!= arr[i-1]){
                return arr[i];
            }
        }
    }
};