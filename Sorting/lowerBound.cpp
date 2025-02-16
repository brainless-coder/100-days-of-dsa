#include<iostream>
using namespace std;

int upperBound(int *arr, int l, int r, int x) {
    int ans = 0;

    while (l <= r) {
        int mid = l + (r - l) / 2;
        
        if (arr[mid] <= x) {
            ans = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    return arr[ans];
}

int lowerBound(int *arr, int l, int r, int x) {
    int ans = 0;

    while(l <= r) {
        int mid = l + (r - l) / 2;

        if (arr[mid] >= x) {
            ans = mid;
            r = mid-1;  
        } else {
            l = mid+1;
        }  
    }

    return arr[ans];
}

int main() {
    int arr[] {2, 3, 5, 6, 8, 8, 8, 10, 12};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x;
    cin >> x;

    cout << lowerBound(arr, 0, n-1, x) << endl;
    cout << upperBound(arr, 0, n-1, x) << endl;

    return 0;
}