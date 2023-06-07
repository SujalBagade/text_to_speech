#include<iostream>
using namespace std;

const int MAX_NODES = 20;

void constructOBST();
void printOptimalBST(int, int);

float a[MAX_NODES], b[MAX_NODES], wt[MAX_NODES][MAX_NODES], c[MAX_NODES][MAX_NODES];
int r[MAX_NODES][MAX_NODES], n;

int main()
{
    cout << "****** PROGRAM FOR OBST ******\n";
    cout << "\nEnter the number of nodes: ";
    cin >> n;

    cout << "\nEnter the probabilities for successful search:\n";
    cout << "————————————————\n";
    for (int i = 1; i <= n; i++)
    {
        cout << "p[" << i << "]: ";
        cin >> a[i];
    }

    cout << "\nEnter the probabilities for unsuccessful search:\n";
    cout << "————————————————–\n";
    for (int i = 0; i <= n; i++)
    {
        cout << "q[" << i << "]: ";
        cin >> b[i];
    }

    constructOBST();
    printOptimalBST(0, n);
    cout << endl;

    return 0;
}

void constructOBST()
{
    for (int i = 0; i < n; i++)
    {
        c[i][i] = 0.0;
        r[i][i] = 0;
        wt[i][i] = b[i];
        wt[i][i + 1] = b[i] + b[i + 1] + a[i + 1];
        c[i][i + 1] = b[i] + b[i + 1] + a[i + 1];
        r[i][i + 1] = i + 1;
    }

    c[n][n] = 0.0;
    r[n][n] = 0;
    wt[n][n] = b[n];

    for (int i = 2; i <= n; i++)
    {
        for (int j = 0; j <= n - i; j++)
        {
            wt[j][j + i] = b[j + i] + a[j + i] + wt[j][j + i - 1];
            c[j][j + i] = 9999;
            for (int l = j + 1; l <= j + i; l++)
            {
                if (c[j][j + i] > (c[j][l - 1] + c[l][j + i]))
                {
                    c[j][j + i] = c[j][l - 1] + c[l][j + i];
                    r[j][j + i] = l;
                }
            }
            c[j][j + i] += wt[j][j + i];
        }
    }

    cout << "\n\nOptimal BST is:\n";
    cout << "w[0][" << n << "]: " << wt[0][n] << endl;
    cout << "c[0][" << n << "]: " << c[0][n] << endl;
    cout << "r[0][" << n << "]: " << r[0][n] << endl;
}

void printOptimalBST(int l1, int r1)
{
    if (l1 >= r1)
        return;
    if (r[l1][r[l1][r1] - 1] != 0)
        cout << "\nLeft child of " << r[l1][r1] << ": " << r[l1][r[l1][r1] - 1];
    if (r[r[l1][r1]][r1] != 0)
        cout << "\nRight child of " << r[l1][r1] << ": " << r[r[l1][r1]][r1];
    printOptimalBST(l1, r[l1][r1] - 1);
    printOptimalBST(r[l1][r1], r1);
}
/*

Real-time Example:
Let's consider an example where we have a sorted list of words in a dictionary and their search probabilities based on the frequency of usage. Suppose we have the following data:

k = ["apple", "banana", "cherry", "date"]
p = [0.1, 0.3, 0.2, 0.4]

Using the algorithm described above, we can construct the optimal binary search tree with the least search cost.

Initialize the cost table with the search probabilities:
cost = [[0, 0.1, 0, 0, 0],
[0, 0, 0.3, 0, 0],
[0, 0, 0, 0.2, 0],
[0, 0, 0, 0, 0.4]]

Calculate the cost of subtrees of length 2:
cost[1][2] = p[1] + p[2] = 0.1 + 0.3 = 0.4
cost[2][3] = p[2] + p[3] = 0.3 + 0.2 = 0.5
cost[3][4] = p[3] + p[4] = 0.2 + 0.4 = 0.6

Calculate the cost of subtrees of length 3:
cost[1][3] = min(cost[1][2] + cost[3][3] + p[1] + p[2] + p[3], cost[1][1] + cost[2][3] + p[1] + p[2] + p[3]) = min(0.4 + 0.2 + 0.1 + 0.3 + 0.2, 0.1 + 0.5 + 0.1 + 0.3 + 0.2) = 1.0
cost[2][4] = min(cost[2][3] + cost[4][4] + p[2] + p[3] + p[4], cost[2][2] + cost[3][4] + p[2] + p[3] + p[4]) = min(0.5 + 0.4 + 0.3 + 0.2 + 0.4, 0.3 + 0.6 + 0.3 + 0.2 + 0.4) = 2.1

Calculate the cost of the complete tree:
cost[1][4] = min(cost[1][3] + cost[4][4] + p[1] + p[2] + p[3] + p[4], cost[1][1] + cost[2][4] + p[1] + p[2] + p[3] + p[4]) = min(1.0 + 0.4 + 0.1 + 0.3 + 0.2 + 0.4, 0.1 + 2.1 + 0.1 + 0.3 + 0.2 + 0.4) = 2.4

Therefore, the minimum search cost for the optimal binary search tree is 2.4.

This algorithm ensures that the keys with higher search probabilities are placed closer to the root of the tree, resulting in faster searches for frequently accessed keys.







*/