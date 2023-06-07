#include <iostream>
#include <string>
using namespace std;

// Node structure for BST
struct Node {
    string keyword;
    string meaning;
    Node* left;
    Node* right;
};

// Function to create a new node
Node* createNode(string keyword, string meaning) {
    Node* newNode = new Node();
    newNode->keyword = keyword;
    newNode->meaning = meaning;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Function to insert a node into BST
Node* insertNode(Node* root, string keyword, string meaning) {
    if (root == NULL)
        return createNode(keyword, meaning);

    if (keyword < root->keyword)
        root->left = insertNode(root->left, keyword, meaning);
    else if (keyword > root->keyword)
        root->right = insertNode(root->right, keyword, meaning);

    return root;
}

// Function to search for a keyword in BST
Node* searchKeyword(Node* root, string keyword, int& comparisons) {
    if (root == NULL || root->keyword == keyword)
        return root;

    if (root->keyword < keyword)
        return searchKeyword(root->right, keyword, ++comparisons);

    return searchKeyword(root->left, keyword, ++comparisons);
}

// Function to find the node with minimum keyword value
Node* findMin(Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

// Function to delete a node from BST
Node* deleteNode(Node* root, string keyword) {
    if (root == NULL)
        return root;

    if (keyword < root->keyword)
        root->left = deleteNode(root->left, keyword);
    else if (keyword > root->keyword)
        root->right = deleteNode(root->right, keyword);
    else {
        // Node with only one child or no child
        if (root->left == NULL) {
            Node* temp = root->right;
            delete root;
            return temp;
        } else if (root->right == NULL) {
            Node* temp = root->left;
            delete root;
            return temp;
        }

        // Node with two children
        Node* temp = findMin(root->right);
        root->keyword = temp->keyword;
        root->meaning = temp->meaning;
        root->right = deleteNode(root->right, temp->keyword);
    }
    return root;
}

// Function to update the value of a keyword
void updateKeyword(Node* root, string keyword, string newMeaning) {
    int comparisons = 0;
    Node* node = searchKeyword(root, keyword, comparisons);

    if (node != NULL) {
        node->meaning = newMeaning;
        cout << "Keyword updated successfully." << endl;
    } else {
        cout << "Keyword not found." << endl;
    }
}

// Function to traverse and display BST in ascending order
void displayAscending(Node* root) {
    if (root == NULL)
        return;

    displayAscending(root->left);
    cout << root->keyword << ": " << root->meaning << endl;
    displayAscending(root->right);
}

// Function to traverse and display BST in descending order
void displayDescending(Node* root) {
    if (root == NULL)
        return;

    displayDescending(root->right);
    cout << root->keyword << ": " << root->meaning << endl;
    displayDescending(root->left);
}

// Function to calculate the maximum comparisons required for finding a keyword
int calculateMaxComparisons(Node* root) {
    if (root == NULL)
        return 0;

    int leftHeight = calculateMaxComparisons(root->left);
    int rightHeight = calculateMaxComparisons(root->right);

    return 1 + max(leftHeight, rightHeight);
}

int main() {
    Node* root = NULL;
    int choice;
    string keyword, meaning;

    while (true) {
        cout << "\n--- Dictionary Menu ---" << endl;
        cout << "1. Add Keyword" << endl;
        cout << "2. Delete Keyword" << endl;
        cout << "3. Update Keyword" << endl;
        cout << "4. Display Dictionary (Ascending)" << endl;
        cout << "5. Display Dictionary (Descending)" << endl;
        cout << "6. Find Maximum Comparisons" << endl;
        cout << "7. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "\nEnter keyword: ";
                cin >> keyword;
                cout << "Enter meaning: ";
                cin.ignore();
                getline(cin, meaning);
                root = insertNode(root, keyword, meaning);
                cout << "Keyword added successfully." << endl;
                break;
            case 2:
                cout << "\nEnter keyword to delete: ";
                cin >> keyword;
                root = deleteNode(root, keyword);
                cout << "Keyword deleted successfully." << endl;
                break;
            case 3:
                cout << "\nEnter keyword to update: ";
                cin >> keyword;
                cout << "Enter new meaning: ";
                cin.ignore();
                getline(cin, meaning);
                updateKeyword(root, keyword, meaning);
                break;
            case 4:
                cout << "\n--- Dictionary (Ascending) ---" << endl;
                displayAscending(root);
                break;
            case 5:
                cout << "\n--- Dictionary (Descending) ---" << endl;
                displayDescending(root);
                break;
            case 6:
                cout << "\nMaximum comparisons: " << calculateMaxComparisons(root) << endl;
                break;
            case 7:
                cout << "\nExiting program..." << endl;
                exit(0);
            default:
                cout << "\nInvalid choice. Please try again." << endl;
        }
    }

    return 0;
}
