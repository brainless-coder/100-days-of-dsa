#include<iostream>
using namespace std;

int fastSearch_naive(int arr[], int l, int r, int n) {
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        if ((arr[i] >= l) && (arr[i] <= r)) 
            ans++;
    }

    return ans;
}

/* int fastSearch(int *arr, int left, int right, int start, int end) {
    int ans = 0;

    while (left <= right) {
        int mid = l + (r - l) / 2;

        if (arr[mid] >= left) {
            if (arr[mid] >= start && arr[mid] <= end) {
                ans++;
            }

        }
    }
} */

int main() {
    int arr[] {10, 2, 10, 5, 3, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    int start, end, left, right;
    cin >> start >> end;

    cout << fastSearch_naive(arr, start, end, n) << endl;
    // cout << fastSearch(arr, 0, n-1, start, end) << endl;

    return 0;
}