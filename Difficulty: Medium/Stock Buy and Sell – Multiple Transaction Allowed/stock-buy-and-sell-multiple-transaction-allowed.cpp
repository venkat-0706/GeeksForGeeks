
class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        // code here
        int n=prices.size();
        int count=0;
        for(int i=1;i<n;i++){
            if(prices[i] > prices[i-1]){
                count+= prices[i]-prices[i-1];
            }
        }
        return count;
    }
};
