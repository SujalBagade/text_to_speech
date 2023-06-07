#include <iostream>
using namespace std;

const int MAX_CITIES = 50;
const int MAX_NAME_LENGTH = 50;

int main()
{
    int n;
    cout << "Enter the number of cities: ";
    cin >> n;

    // Validate the input
    if (n <= 0 || n > MAX_CITIES)
    {
        cout << "Invalid number of cities." << endl;
        return 1;
    }

    string city[MAX_CITIES];
    int adj_matrix[MAX_CITIES][MAX_CITIES];

    // Prompt the user to enter city names
    for (int i = 0; i < n; i++)
    {
        cout << "Enter the name of city " << i + 1 << ": ";
        cin >> city[i];
    }

    // Prompt the user to enter travel times
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            cout << "Enter the time required to travel from " << city[i] << " to " << city[j] << ": ";
            cin >> adj_matrix[i][j];

            // Validate the input
            if (adj_matrix[i][j] <= 0)
            {
                cout << "Invalid travel time." << endl;
                return 1;
            }

            adj_matrix[j][i] = adj_matrix[i][j];
        }
    }

    // Display the adjacency matrix
    cout << "\nAdjacency Matrix:\n\n";
    cout << "\t";
    for (int i = 0; i < n; i++)
    {
        cout << city[i] << "\t";
    }
    cout << endl;

    for (int i = 0; i < n; i++)
    {
        cout << city[i] << "\t";
        for (int j = 0; j < n; j++)
        {
            cout << adj_matrix[i][j] << "\t";
        }
        cout << endl;
    }

    return 0;
}
