//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution 
{
  public:
    vector<int> countDistinct(vector<int> &arr, int k) 
    {
        // code here.
        vector<int> a;
        unordered_map<int ,int>f;
        int n  = arr.size();
        
        for(int i=0;i<k;i++)
        {
            f[arr[i]]++;
        }
        
        a.push_back(f.size());
        
        for(int i=k;i<n;i++)
        {
            f[arr[i-k]]--;
            
            if(f[arr[i-k]] == 0)
            {
                f.erase(arr[i-k]);
            }
            
            f[arr[i]]++;
            
            a.push_back(f.size());
        }
        
        return a;
    }
};

//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        string ks;
        getline(cin, ks);
        int k = stoi(ks);
        Solution obj;
        vector<int> res = obj.countDistinct(arr, k);
        for (auto it : res)
            cout << it << " ";
        cout << endl;
        cout << "~"
             << "\n";
    }

    return 0;
}

// } Driver Code Ends