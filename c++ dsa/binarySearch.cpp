#include<bits/stdc++.h>
using namespace std;

int binarySearchIterative(int arr[], int n, int x) {
    int l = 0, r = n-1, ele = -1;

    while(l <= r) {
        int mid = (l+r)/2;

        if (arr[mid] > x) {
            r = mid-1;
        } else if (arr[mid] < x) {
            l = mid+1;
        } else {
            ele = mid;
            break;
        }
        
    }

    return ele;
}

int binarySearchRecursive(int arr[], int l, int r, int x) {
    int mid = (l+r) / 2;

    if (l > r) {
        return -1;
    }

    if (arr[mid] > x) {
        return binarySearchRecursive(arr, l, mid-1, x);
    } else if (arr[mid] < x) {
        return binarySearchRecursive(arr, mid+1, r, x);
    } else {
        return mid;
    }

}

int leftOcc(int arr[], int n, int x) {
    int l = 0, r = n-1, ele = -1;

    while(l <= r) {
        int mid = (l+r) / 2;

        if ((arr[mid] == x) && (mid == 0 || arr[mid-1] != x)) {
            ele = mid;
            break;
        } else if (arr[mid] >= x) {
            r = mid-1;
        } else {
            l = mid+1;
        }
    }

    return ele;
}

int rightOcc(int arr[], int n, int x) {
    int l = 0, r = n-1, ele = -1;

    while(l <= r) {
        int mid = (l+r) / 2;

        if ((arr[mid] == x) && (mid == n-1 || arr[mid+1] != x)) {
            ele = mid;
            break;
        } else if (arr[mid] > x) {
            r = mid-1;
        } else {
            l = mid+1;
        }
    }

    return ele;
}

int countOcc(int arr[], int n, int x) {
    int l = leftOcc(arr, n, x);
    int r = rightOcc(arr, n, x);
    int count = r-l+1;

    return count;
}

int count_1_in_BinaryArray(int arr[], int n, int x) {
    int left = leftOcc(arr, n, x);

    return n-left;
}

int findInfSizeArr(int arr[], int n, int x) {
    if (arr[0] == x)
        return 0;

    int i = 1;
    while (arr[i] < x) 
        i *= 2;

    if (arr[i] == x)
        return i;
    
    return binarySearchRecursive(arr, (i/2)-1, i, x);

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

    // cout << binarySearchIterative(arr, n, x) << endl;
    // cout << binarySearchRecursive(arr, 0, n-1, x) << endl;
    // cout << leftOcc(arr, n, x) << endl;
    // cout << rightOcc(arr, n, x) << endl;
    // cout << countOcc(arr, n, x) << endl;
    // cout << count_1_in_BinaryArray(arr, n, x) << endl;
    cout << findInfSizeArr(arr, n, x) << endl;


    return 0;
}