//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public: 
    double distance(int x,int y){
        
        int  xCoordinate = x*x;
        int  yCoordinate = y*y;
        
        return pow(xCoordinate+yCoordinate,0.5);
    }
    static bool comparison(pair<int,double>a,pair<int,double>b){
        
        return a.second<b.second;
    }
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        
        vector<pair<int,double>>ans;
        
        for(int i=0;i<points.size();i++){
            
            //first signifies index, second signifies distance from origin
            int abcissa = points[i][0];
            int ordinate= points[i][1];
            
            ans.push_back({i,distance(abcissa,ordinate)});
        }
        
        sort(ans.begin(),ans.end(),comparison);//sorted on basis of distance from origin
        
        vector<vector<int>>resultant;
        
        for(int i=0;i<k;i++){
            
            int index = ans[i].first;
            resultant.push_back(points[index]);
        }
        
        return resultant;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int k;
        cin >> k;
        int n;
        cin >> n;
        vector<vector<int>> points(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> points[i][0] >> points[i][1];
        }
        Solution ob;
        vector<vector<int>> ans = ob.kClosest(points, k);
        sort(ans.begin(), ans.end());
        for (const vector<int>& point : ans) {
            cout << point[0] << " " << point[1] << endl;
        }
        cout << "~" << endl;
    }

    return 0;
}

// } Driver Code Ends