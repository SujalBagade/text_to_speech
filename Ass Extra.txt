#include <iostream>
using namespace std;

// Node structure for the expression tree
struct Node {
    char data;
    Node* left;
    Node* right;
};

// Function to create a new node
Node* createNode(char value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->left = newNode->right = nullptr;
    return newNode;
}

// Function to check if a character is an operator
bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/');
}

// Function to construct expression tree from prefix expression
Node* constructExpressionTree(string prefix) {
    int len = prefix.length();
    Node* stack[len];
    int top = -1;
    
    // Traverse the prefix expression from right to left
    for (int i = len - 1; i >= 0; i--) {
        char c = prefix[i];
        
        // If current character is an operator
        if (isOperator(c)) {
            Node* newNode = createNode(c);
            newNode->left = stack[top];
            newNode->right = stack[top - 1];
            
            // Pop the top two nodes from the stack
            top -= 2;
            
            // Push the new node onto the stack
            stack[++top] = newNode;
        }
        else {
            // If current character is an operand, push it onto the stack
            stack[++top] = createNode(c);
        }
    }
    
    // The final remaining node in the stack will be the root of the expression tree
    return stack[top];
}

// Function to traverse the expression tree using post-order traversal (non-recursive)
void postOrderTraversal(Node* root) {
    if (root == nullptr)
        return;
    
    Node* stack1[100];
    Node* stack2[100];
    int top1 = -1;
    int top2 = -1;
    
    // Push the root node onto the first stack
    stack1[++top1] = root;
    
    // Run the loop while the first stack is not empty
    while (top1 != -1) {
        // Pop a node from the first stack
        Node* temp = stack1[top1--];
        
        // Push the popped node to the second stack
        stack2[++top2] = temp;
        
        // Push the left and right children of the popped node onto the first stack
        if (temp->left)
            stack1[++top1] = temp->left;
        if (temp->right)
            stack1[++top1] = temp->right;
    }
    
    // Print the nodes in post-order from the second stack
    while (top2 != -1) {
        Node* temp = stack2[top2--];
        cout << temp->data << " ";
        
        // Delete the node
        delete temp;
    }
}

// Function to delete the entire tree
void deleteTree(Node* root) {
    if (root == nullptr)
        return;
    
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

int main() {
    string prefix;
    cout << "Enter the prefix expression: ";
    cin >> prefix;
    
    Node* root = constructExpressionTree(prefix);
    
    cout << "Post-order traversal: ";
    postOrderTraversal(root);
    cout << endl;
    
    // Delete the entire tree
    deleteTree(root);
    
    return 0;
}
