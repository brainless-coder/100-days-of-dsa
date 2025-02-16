#include<bits/stdc++.h>
using namespace std;

void reverseArray(int arr[], int n) {
    int l = 0, r = n-1;

    while (l <= r) {
        swap(arr[l++], arr[r--]);
    }
}

void recursiveRev(int arr[], int l, int r) {
    if (l >= r)
        return;

    swap(arr[l++], arr[r--]);

    return recursiveRev(arr, l, r);
}

void rotateArray(int arr[], int n, int d, char dir) {
    if (dir == 'l' || dir == 'L') {
        reverse(arr, arr+d);
        reverse(arr+d, arr+n);
    } else if (dir == 'r' || dir == 'R') {
        reverse(arr, arr+n-d);
        reverse(arr+n-d, arr+n);
    }

    reverse(arr, arr+n);
}

int main() {
    int arr[] {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    // reverse(arr, arr+size);
    // rotate(arr, arr+2, arr+size);

    // reverseArray(arr, size);
    // recursiveRev(arr, 0, size-1);

    rotateArray(arr, size, 2, 'r');

    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}