// User function template for C++
class Solution {
  public:
    // Function to return sum of elements
    int arraySum(vector<int>& arr) {
        // code here
        int sum=0;
        int n=arr.size();
        for(int i=0;i<n;i++){
            sum += arr[i];
        }
        return sum;
    }
};