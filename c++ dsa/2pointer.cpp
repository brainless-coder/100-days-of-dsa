#include<bits/stdc++.h>
using namespace std;

void pairSum(int arr[], int n, int x) {
    int l = 0, r = n-1, a = -1, b = -1;

    while (l < r) {
        int sum = arr[l] + arr[r];

        if (sum == x) {
            a = arr[l], b = arr[r];
            break;
        } else if (sum > x) {
            r--;
        } else {
            l++;
        }
    }

    cout << a << " " << b << endl;
}

bool isPair(int arr[], int l, int r, int x) {
    while (l < r) {
        int sum = arr[l] + arr[r];

        if (sum == x) {
            cout << arr[l] << " " << arr[r] << " ";
            return true;
        } else if (sum > x) {
            r--;
        } else {
            l++;
        }
    }

    return false;

}

void triplet(int arr[], int n, int x) {
    for (int i = 0; i < n; ++i) {
        if (isPair(arr, i+1, n-1, x-arr[i]) == true) {
            cout << arr[i] << endl;
        }
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    
    int n, x;
    cin >> n >> x;

    int arr[n];

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    // pairSum(arr, n, x);
    triplet(arr, n, x);

    return 0;
}