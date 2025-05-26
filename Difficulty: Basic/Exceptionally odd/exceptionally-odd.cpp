// User function template for C++

class Solution {
  public:
    int getOddOccurrence(int arr[], int n) {
        // code here
        int count =0;
        for(int i=0;i<n;i++){
            count ^= arr[i];
        }
        return count;
    }
};