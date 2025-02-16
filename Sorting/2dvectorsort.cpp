#include<bits/stdc++.h>
using namespace std;

bool sortColVec(const vector<int> &v1, const vector<int> &v2) {
    return v1[1] < v2[1];
}

bool sortColArr(int v1[], int v2[]) {
    cout << v1[0] << " " << v2[0] << endl;
    return v1[0] < v2[0];
}

int main() {
    vector< vector<int> > vect {
        {4, 8, 9},
        {7, 3, 1},
        {2, 6, 5}
    };

    int arr[3][3] = {
        {5, 1, 9},
        {7, 3, 1},
        {6, 4, 2}
    };
    int n = sizeof(arr)/ sizeof(arr[0]);
    int m = sizeof(arr[0])/ sizeof(arr[0][0]);

    // sorting a particular row
    // sort(vect[0].begin(), vect[0].end());

    // sorting the entrire vector based on a column, can be achieved by using a custome comparator
    // sort(vect.begin(), vect.end(), sortColVec);

    /* agar apan puure vector pe sort ka use kaare bina kisi comparator ke then ye 
    1st column ke according sort karega */
    // sort(vect.begin(), vect.end());

    // Displaying the whole vector
    // for (int i = 0; i < vect.size(); ++i) {
    //     for (int j = 0; j < vect[i].size(); ++j) 
    //         cout << vect[i][j] << " ";
    //     cout << endl;
    // }

    // sorting a particular row
    // sort(arr[0], arr[0]+m);
    // sort(arr[1], arr[1]+m);
    // sort(arr[2], arr[2]+m);

    // sorting the entire array
    sort(arr, arr+n, sortColArr);

    // Displaying the whole array
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j)
            cout << arr[i][j] << " ";
        cout << endl;
    }

    return 0;
}