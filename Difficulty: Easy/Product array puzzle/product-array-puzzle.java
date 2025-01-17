//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t > 0) {
            String inputLine[] = br.readLine().trim().split(" ");
            int n = inputLine.length;
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            Solution ob = new Solution();
            int[] ans = new int[n];
            ans = ob.productExceptSelf(arr);

            for (int i = 0; i < n; i++) {
                System.out.print(ans[i] + " ");
            }
            System.out.println();
            System.out.println("~");
            t--;
        }
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    public static int[] productExceptSelf(int arr[]) {
        // code here
        int n=arr.length;
        int [] res=new int[n];
        int[] arrL=new int[n];
        int[] arrR=new int[n];
        int product=1;
        for(int i=0;i<n;i++){
            product*=arr[i];
            arrL[i]=product;
        }
        int newproduct=1;
        for(int i=n-1;i>=0;i--){
            newproduct*=arr[i];
            arrR[i]=newproduct;
        }
        for(int i=1;i<n-1;i++){
            res[i]=arrL[i-1]*arrR[i+1];
        }
        res[0]=arrR[1];
        res[n-1]=arrL[n-2];
        return res;
        
    }
}
