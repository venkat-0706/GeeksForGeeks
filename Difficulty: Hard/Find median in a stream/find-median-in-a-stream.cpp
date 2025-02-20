//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    vector<double> getMedian(vector<int> &arr) {
        vector<double>ans;
        vector<int>vec;
        vec.push_back(arr[0]);
        ans.push_back(arr[0]);
        for(int i=1;i<arr.size();i++){
            
            int ele=arr[i];
            int idx=lower_bound(vec.begin(),vec.end(),ele)-vec.begin();
            if(idx==vec.size())
            vec.push_back(ele);
            else
            vec.insert(vec.begin()+idx,ele);
            if(vec.size()%2){
                ans.push_back(vec[vec.size()/2]);
            }
            else{
                int idx1=vec.size()/2-1;
                int idx2=vec.size()/2;
                double num=double(vec[idx1]+vec[idx2])/2;
                ans.push_back(num);
            }
        }
        
        return ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        string s;
        getline(cin, s);
        stringstream ss(s);
        vector<int> nums;
        int num;
        while (ss >> num) {
            nums.push_back(num);
        }
        Solution ob;
        vector<double> ans = ob.getMedian(nums);
        cout << fixed << setprecision(1);
        for (auto &i : ans)
            cout << i << " ";
        cout << "\n";
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends