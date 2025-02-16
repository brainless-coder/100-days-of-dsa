#include<bits/stdc++.h>
using namespace std;

bool sortCol(int v1[], int v2[]) {
    return v1[0] < v2[0];
}

int main() {
    int arr[][3] {
        {4, 9, 6},
        {1, 2, 5},
        {3, 8, 7}
    };
    int n = sizeof(arr) / sizeof(arr[0]);
    int m = sizeof(arr[0]) / sizeof(arr[0][0]);

    sort(arr[0], arr[0]+n);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}