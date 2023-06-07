#include <iostream>
#include <vector>
using namespace std;

// Structure for storing (key, value) pairs
struct KeyValuePair {
    int key;
    string value;
};

// Hash dictionary class
class HashDictionary {
private:
    vector<vector<KeyValuePair>> buckets;  // Array of buckets
    int size;  // Size of the dictionary

public:
    // Constructor
    HashDictionary(int capacity) {
        buckets.resize(capacity);
        size = capacity;
    }

    // Hash function to calculate the bucket index
    int hashFunction(int key) {
        return key % size;
    }

    // Insert a (key, value) pair into the dictionary
    void insert(int key, string value) {
        int index = hashFunction(key);
        vector<KeyValuePair>& bucket = buckets[index];
        
        // Check if the key already exists in the bucket
        for (KeyValuePair& kvp : bucket) {
            if (kvp.key == key) {
                kvp.value = value;  // Update the value
                cout << "Key updated successfully." << endl;
                return;
            }
        }
        
        // Add a new (key, value) pair to the bucket
        bucket.push_back({key, value});
        cout << "Key inserted successfully." << endl;
    }

    // Find the value associated with a key in the dictionary
    string find(int key) {
        int index = hashFunction(key);
        vector<KeyValuePair>& bucket = buckets[index];
        
        // Search for the key in the bucket
        for (const KeyValuePair& kvp : bucket) {
            if (kvp.key == key) {
                return kvp.value;  // Found the key, return the value
            }
        }
        
        return "";  // Key not found
    }

    // Delete a (key, value) pair from the dictionary
    void remove(int key) {
        int index = hashFunction(key);
        vector<KeyValuePair>& bucket = buckets[index];
        
        // Search for the key in the bucket
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if ((*it).key == key) {
                bucket.erase(it);  // Remove the key-value pair
                cout << "Key deleted successfully." << endl;
                return;
            }
        }
        
        cout << "Key not found." << endl;
    }
};

// Display menu and get user choice
int getMenuChoice() {
    int choice;
    cout << "\n--- Dictionary Menu ---" << endl;
    cout << "1. Insert a key-value pair" << endl;
    cout << "2. Find value for a key" << endl;
    cout << "3. Delete a key-value pair" << endl;
    cout << "4. Exit" << endl;
    cout << "Enter your choice: ";
    cin >> choice;
    return choice;
}

int main() {
    int capacity;
    cout << "Enter the capacity of the dictionary: ";
    cin >> capacity;

    HashDictionary dictionary(capacity);
    int key;
    string value;

    int choice = getMenuChoice();

    while (choice != 4) {
        switch (choice) {
            case 1:
                cout << "Enter key: ";
                cin >> key;
                cout << "Enter value: ";
                cin.ignore();
                getline(cin, value);
                dictionary.insert(key, value);
                break;
            case 2:
                cout << "Enter key to find value: ";
                cin >> key;
                value = dictionary.find(key);
                if (!value.empty()) {
                    cout << "Value for key " << key << ": " << value << endl;
                } else {
                    cout << "Key not found." << endl;
                }
                break;
            case 3:
                cout << "Enter key to delete: ";
                cin >> key;
                dictionary.remove(key);
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
                break;
        }

        choice = getMenuChoice();
    }

    return 0;
}
