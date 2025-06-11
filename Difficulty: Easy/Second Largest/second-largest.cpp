class Solution {
  public:
    int getSecondLargest(vector<int> &arr) {
        // code here
        int lar=-1, res=-1;
        for(int i=0;i<arr.size();i++){
            if(arr[i] > lar){
                res=lar;
                lar=arr[i];
            } else if(arr[i] < lar && arr[i]> res){
                res=arr[i];
            }
        }
        return res;
    }
};