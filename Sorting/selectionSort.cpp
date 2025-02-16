#include<iostream>
using namespace std;

void selectionSort(int arr[], int n) {

    for (int i = 0; i < n-1; ++i) {
        int min_idx = i;

        for (int j = i+1; j < n; ++j) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        swap(arr[min_idx], arr[i]);
    }
}

int main() {
    int arr[] {4, 2, 1, 6, 8, 9, 0, 12, 5};
    int n = sizeof(arr)/sizeof(arr[0]);

    selectionSort(arr, n);

    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }

    return 0;
}