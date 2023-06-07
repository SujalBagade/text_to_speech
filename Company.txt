#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;


const int MAX_NAME_LENGTH = 50;
const int MAX_DESIGNATION_LENGTH = 50;

// Structure for employee information
struct Employee {
    int id;
    char name[MAX_NAME_LENGTH];
    char designation[MAX_DESIGNATION_LENGTH];
    double salary;
};

// Function to add employee information
void addEmployee(fstream& file) {
    Employee employee;

    cout << "Enter Employee ID: ";
    cin >> employee.id;
    cout << "Enter Employee Name: ";
    cin.ignore();
    cin.getline(employee.name, MAX_NAME_LENGTH);
    cout << "Enter Employee Designation: ";
    cin.getline(employee.designation, MAX_DESIGNATION_LENGTH);
    cout << "Enter Employee Salary: ";
    cin >> employee.salary;

    file.write(reinterpret_cast<char*>(&employee), sizeof(Employee));

    cout << "Employee information added successfully.\n";
}

// Function to delete employee information
void deleteEmployee(fstream& file) {
    int id;
    cout << "Enter Employee ID to delete: ";
    cin >> id;

    fstream tempFile("temp.dat", ios::out | ios::binary);

    Employee employee;
    while (file.read(reinterpret_cast<char*>(&employee), sizeof(Employee))) {
        if (employee.id != id) {
            tempFile.write(reinterpret_cast<char*>(&employee), sizeof(Employee));
        }
    }

    file.close();
    tempFile.close();

    remove("employee.dat");
    rename("temp.dat", "employee.dat");

    cout << "Employee information deleted successfully.\n";
}

// Function to display employee information
void displayEmployee(fstream& file) {
    int id;
    cout << "Enter Employee ID to display: ";
    cin >> id;

    Employee employee;
    bool found = false;

    while (file.read(reinterpret_cast<char*>(&employee), sizeof(Employee))) {
        if (employee.id == id) {
            cout << "Employee ID: " << employee.id << endl;
            cout << "Employee Name: " << employee.name << endl;
            cout << "Employee Designation: " << employee.designation << endl;
            cout << "Employee Salary: " << employee.salary << endl;
            found = true;
            break;
        }
    }

    if (!found) {
        cout << "Employee not found.\n";
    }
}

// Function to display the menu
void displayMenu() {
    cout << "Menu:\n";
    cout << "1. Add Employee\n";
    cout << "2. Delete Employee\n";
    cout << "3. Display Employee\n";
    cout << "4. Exit\n";
    cout << "Enter your choice: ";
}

int main() {
    fstream file("employee.dat", ios::in | ios::out | ios::binary);

    if (!file) {
        cout << "Failed to open file.\n";
        return 1;
    }

    int choice;
    while (true) {
        displayMenu();
        cin >> choice;

        switch (choice) {
            case 1:
                addEmployee(file);
                break;
            case 2:
                deleteEmployee(file);
                break;
            case 3:
                displayEmployee(file);
                break;
            case 4:
                cout << "Exiting the program...\n";
                file.close();
                return 0;
            default:
                cout << "Invalid choice. Please try again.\n";
        }

        cout << endl;
    }
}
