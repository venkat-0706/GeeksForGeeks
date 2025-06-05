// User function Template for C++

class Solution {
  public:
    void bkt(int st, vector<int>& arr,vector<int>&v1, vector<vector<int>>&v){
        v.push_back(v1);
        for(int i=st; i<arr.size(); i++){
            v1.push_back(arr[i]);
            bkt(i+1,arr,v1,v);
            v1.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& arr) {
        // code here
        sort(arr.begin(),arr.end());
        vector<vector<int>>v;
        vector<int>v1;
        bkt(0,arr,v1,v);
        return v;
    }
};



