#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

// Function to create a new node
Node* createNode(int value) {
    Node* newNode = new Node();
    if (newNode == nullptr) {
        cout << "Memory allocation failed!" << endl;
        return nullptr;
    }
    newNode->data = value;
    newNode->left = nullptr;
    newNode->right = nullptr;
    return newNode;
}

// Function to insert a new node in the BST
Node* insertNode(Node* root, int value) {
    if (root == nullptr) {
        return createNode(value);
    }
    if (value < root->data) {
        root->left = insertNode(root->left, value);
    } else if (value > root->data) {
        root->right = insertNode(root->right, value);
    }
    return root;
}

// Function to find the number of nodes in the longest path
int findLongestPath(Node* root) {
    if (root == nullptr) {
        return 0;
    }
    int leftPath = findLongestPath(root->left);
    int rightPath = findLongestPath(root->right);
    return 1 + max(leftPath, rightPath);
}

// Function to find the minimum data value in the tree
int findMinimumValue(Node* root) {
    if (root == nullptr) {
        cout << "Tree is empty!" << endl;
        return -1; // Assuming -1 as an invalid value
    }
    if (root->left == nullptr) {
        return root->data;
    }
    return findMinimumValue(root->left);
}

// Function to swap the left and right pointers at every node
void swapPointers(Node* root) {
    if (root == nullptr) {
        return;
    }
    swap(root->left, root->right);
    swapPointers(root->left);
    swapPointers(root->right);
}

// Function to search for a value in the BST
bool searchValue(Node* root, int value) {
    if (root == nullptr) {
        return false;
    }
    if (root->data == value) {
        return true;
    }
    if (value < root->data) {
        return searchValue(root->left, value);
    } else {
        return searchValue(root->right, value);
    }
}

// Function to display the menu options
void displayMenu() {
    cout << "-----------------------------" << endl;
    cout << "Binary Search Tree Operations" << endl;
    cout << "-----------------------------" << endl;
    cout << "1. Insert a new node" << endl;
    cout << "2. Find the number of nodes in the longest path" << endl;
    cout << "3. Find the minimum data value in the tree" << endl;
    cout << "4. Change the tree to swap left and right pointers" << endl;
    cout << "5. Search for a value in the tree" << endl;
    cout << "6. Exit" << endl;
    cout << "-----------------------------" << endl;
}

int main() {
    Node* root = nullptr;
    int choice;

    do {
        displayMenu();
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int value;
                cout << "Enter the value to insert: ";
                cin >> value;
                root = insertNode(root, value);
                cout << "Node inserted successfully!" << endl;
                break;
            }
            case 2: {
                int longestPath = findLongestPath(root);
                cout << "Number of nodes in the longest path: " << longestPath << endl;
                break;
            }
            case 3: {
                int minValue = findMinimumValue(root);
                cout << "Minimum data value in the tree: " << minValue << endl;
                break;
            }
            case 4: {
                swapPointers(root);
                cout << "Tree modified successfully!" << endl;
                break;
            }
            case 5: {
                int value;
                cout << "Enter the value to search: ";
                cin >> value;
                bool isFound = searchValue(root, value);
                if (isFound) {
                    cout << "Value " << value << " found in the tree." << endl;
                } else {
                    cout << "Value " << value << " not found in the tree." << endl;
                }
                break;
            }
            case 6:
                cout << "Exiting the program..." << endl;
                break;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
        cout << endl;

    } while (choice != 6);

    return 0;
}
