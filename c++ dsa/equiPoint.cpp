#include<iostream>
#include<algorithm>
#include<numeric>
using namespace std;

void preSuffix(int arr[], int n) {
    int preSum[n] {}, suffSum[n] {};

    preSum[0] = arr[0];
    for (int i = 1; i < n; ++i) {
        preSum[i] = preSum[i-1] + arr[i];
    }

    suffSum[n-1] = arr[n-1];
    for (int i = n-2; i >= 0; --i) {
        suffSum[i] = suffSum[i+1] + arr[i];
    }

    for (int i = 0; i < n; ++i) {
        if (preSum[i] == suffSum[i]) {
            cout << "YES at index: " << i << endl;
            return;
        }
    }

    cout << "NO\n";
}

void optimizedApproach(int arr[], int n) {
    int total {}, left {}, right {};
    total = accumulate(arr, arr+n, total);

    for (int i = 0; i < n; ++i) {
        right = total - left;
        left += arr[i];

        if (left == right) {
            cout << "YES at index: " << i << endl;
            return;
        }
    }

    cout << "NO\n";
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif  

    int t, n;
    cin >> t;

    while (t--) {
        cin >> n;
        int arr[n];

        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        // preSuffix(arr, n);
        optimizedApproach(arr, n);
    }

    return 0;
}