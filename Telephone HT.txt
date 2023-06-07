#include <iostream>
#include <string>
using namespace std;

const int TABLE_SIZE = 100;

struct Client {
    string name;
    string phoneNumber;
};

class TelephoneBook {
private:
    Client hashtable[TABLE_SIZE];

public:
    int hashFunction(const string& name) {
        int hash = 0;
        for (char ch : name) {
            hash += ch;
        }
        return hash % TABLE_SIZE;
    }

    void addClient(const string& name, const string& phoneNumber) {
        int index = hashFunction(name);
        hashtable[index].name = name;
        hashtable[index].phoneNumber = phoneNumber;
    }

    void searchClient(const string& name) {
        int index = hashFunction(name);
        if (hashtable[index].name == name) {
            cout << "Client Found: " << name << endl;
            cout << "Phone Number: " << hashtable[index].phoneNumber << endl;
        } else {
            cout << "Client Not Found: " << name << endl;
        }
    }
};

int main() {
    TelephoneBook telephoneBook;
    string name, phoneNumber;
    char choice;

    do {
        cout << "1. Add Client\n";
        cout << "2. Search Client\n";
        cout << "3. Quit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case '1':
                cout << "Enter client name: ";
                cin.ignore();
                getline(cin, name);
                cout << "Enter client phone number: ";
                getline(cin, phoneNumber);
                telephoneBook.addClient(name, phoneNumber);
                cout << "Client added successfully!\n";
                break;
            case '2':
                cout << "Enter client name to search: ";
                cin.ignore();
                getline(cin, name);
                telephoneBook.searchClient(name);
                break;
            case '3':
                cout << "Quitting program...\n";
                break;
            default:
                cout << "Invalid choice! Please try again.\n";
        }

        cout << endl;

    } while (choice != '3');

    return 0;
}
