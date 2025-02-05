//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Definition of the Node class
class Node {
  public:
    int data;
    Node *left;
    Node *right;

    Node(int x) {
        data = x;
        left = NULL;
        right = NULL;
    }
};

// Function to print the tree in postorder traversal
void printPostOrder(Node *root) {
    if (root == NULL)
        return;
    printPostOrder(root->left);
    printPostOrder(root->right);
    cout << root->data << " ";
}


// } Driver Code Ends
// Class that contains the logic to build the binary tree
/*
Definition of the Node class
class Node {
public:
    int data;
    Node *left;
    Node *right;

    Node(int x) {
        data = x;
        left = NULL;
        right = NULL;
    }
};
*/
class Solution {
    Node *akshu(vector<int> &i,vector<int> &p,unordered_map<int,int> &u,int s,int e, int &t)
    {
        if(s>e)
        {
            return NULL;
        }
        int r = p[t++];
        Node *root = new Node(r);
        int ri = u[r];
       
        root->left = akshu(i,p,u,s,ri - 1,t);
        root-> right = akshu(i,p,u,ri + 1,e,t);
        
        return root;
    }
    
  public:
    Node *buildTree(vector<int> &inorder, vector<int> &preorder) 
    {
        // Code here
        unordered_map<int,int>oye;
        for(int i=0;i<inorder.size();i++)
        {
            oye[inorder[i]] = i;
        }
        
        int t = 0;
        return akshu(inorder,preorder,oye,0,inorder.size()-1,t);
    }
};

//{ Driver Code Starts.

// Main function where the test cases are handled
int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        vector<int> inorder, preorder;

        // Input the inorder traversal
        string input;
        getline(cin, input);
        stringstream ss1(input);
        int num;
        while (ss1 >> num)
            inorder.push_back(num);

        // Input the preorder traversal
        getline(cin, input);
        stringstream ss2(input);
        while (ss2 >> num)
            preorder.push_back(num);

        // Create Solution object and build the tree
        Solution obj;
        Node *root = obj.buildTree(inorder, preorder);

        // Print the postorder traversal of the constructed tree
        printPostOrder(root);
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends