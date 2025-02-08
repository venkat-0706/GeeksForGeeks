//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
#define MAX_HEIGHT 100000

// Tree Node
class Node {
  public:
    int data;
    Node* left;
    Node* right;

    // Constructor to initialize a new node
    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};

// Utility function to create a new Tree Node
Node* newNode(int val) {
    return new Node(val);
}

// Function to Build Tree
Node* buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after splitting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node* root = newNode(stoi(ip[0]));

    // Push the root to the queue
    queue<Node*> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node* currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current node
            currNode->left = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current node
            currNode->right = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
/*
// Tree Node
class Node {
  public:
    int data;
    Node* left;
    Node* right;

    // Constructor to initialize a new node
    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};
*/


class Solution {
  public:
    
    vector<int> ans;
    
    // inserts all the left nodes except the leaf nodes
    void leftInsert(Node* root){
        // inserting the current node
        if(root->left!=NULL || root->right!=NULL) ans.push_back(root->data);
        // conditional recursive calls (base case handled)
        if(root->left!=NULL) leftInsert(root->left);
        else if(root->right!=NULL) leftInsert(root->right);
        else return;
    }
    
    // inserts all the leaf nodes
    void bottomInsert(Node* root){
        // base case
        if(root->left==NULL && root->right==NULL){
            ans.push_back(root->data);
        }
        // recursive calls, first left then right
        if(root->left) bottomInsert(root->left);
        if(root->right) bottomInsert(root->right);
    }
    
    // inserts all the right nodes except the leaf nodes
    void rightInsert(Node* root){
        // conditional recursive calls (base case handled)
        if(root->right!=NULL) rightInsert(root->right);
        else if(root->left!=NULL) rightInsert(root->left);
        else return;
        // inserting the current node
        ans.push_back(root->data);
    }
    
    vector<int> boundaryTraversal(Node *root) {
        // code here
        
        if(root==NULL) return ans;
        
        ans.push_back(root->data);
        
        if(root->left==NULL && root->right==NULL) return ans;
        
        // left sub-tree exists ??
        if(root->left!=NULL){
            leftInsert(root->left);
        }
        
        bottomInsert(root);
        
        // right sub-tree exist??
        if(root->right!=NULL){
            rightInsert(root->right);
        }
        
        
        return ans;
    }
};

//{ Driver Code Starts.

/* Driver program to test size function */
int main() {
    int t;
    string tc;
    getline(cin, tc);
    t = stoi(tc);
    while (t--) {
        string s, ch;
        getline(cin, s);
        Node* root = buildTree(s);
        Solution ob;
        vector<int> res = ob.boundaryTraversal(root);
        for (int i : res)
            cout << i << " ";
        cout << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends