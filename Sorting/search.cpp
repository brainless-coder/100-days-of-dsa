#include<iostream>
using namespace std;

void linearSearch(int arr[], int n, int x) {
    int i;

    for (i = 0; i < n; ++i) {
        if (arr[i] == x) {
            cout << i << endl;
            break;
        }
    }

    if (i == n) {
        cout << "Element not present in array\n";
    }
}


int binarySearch(int *arr, int l, int r, int x) {
    int mid;

    while (l <= r) {
        mid = l + (r-l) / 2;

        if (arr[mid] < x) {
            l  = mid+1;
        } else if (arr[mid] > x) {
            r = mid-1;;
        } else if (arr[mid] == x) {
            return mid;
        }
    }

    return -1;
}


int main() {
    int a[] {1, 5, 7, 0 ,7, 5, 3, 2, 1, 6};
    int b[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 12};
    int lenA = sizeof(a) / sizeof(a[0]);
    int lenB = sizeof(b) / sizeof(b[0]);

    // linearSearch(a, lenA, 34);
    cout << binarySearch(b, 0, lenB-1, 2) << endl;

    return 0;
}