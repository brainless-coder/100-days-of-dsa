#include<bits/stdc++.h>
using namespace std;

int solve(int arr[], int n) {
    int res {};

    for (int i = 0; i < n; ++i) {
        for (int j = i+1; j < n; ++j) {
            if (arr[j] < arr[i]) {
                break;
            }

            if (arr[j] > arr[i] && arr[j+1] < arr[j]) {
                res += arr[j] - arr[i];
                i = j;
                break;
            }
        }
    }

    return res;
}

int main() {
    // int arr[] {1, 5, 3, 8, 12};
    // int arr[] {1, 2, 5};
    // int arr[] {5, 2, 1};
    int arr[] {100, 180, 260, 310, 40, 535, 695};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << solve(arr, n) << endl;
    
    return 0;
}