#include<bits/stdc++.h>
using namespace std;

int slidingWindow(int arr[], int n, int k) {
    int i {}, j {}, sum {}, maxSum = INT_MIN;

    while (j < n) {
        sum += arr[j];
        if (j-i+1 < k) {
            j++;
        } else if (j-i+1 == k) {
            maxSum = max(sum, maxSum);
            sum -= arr[i];
            i++;
            j++;
        }
    }

    return maxSum;
}

int main() {
    int arr[] {2, 3, 5, 2, 9, 7, 1};
    int n = sizeof(arr) /  sizeof(arr[0]);
    int k = 3;

    cout << slidingWindow(arr, n, k) << endl;

    return 0;
}