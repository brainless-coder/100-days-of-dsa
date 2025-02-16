#include<iostream>
using namespace std;

void sort(int *arr, int length) {
    int i, j, key;

    for (int i = 1; i < length; ++i) {
        key = arr[i];
        j = i-1;

        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }

        arr[j+1] = key;
    }
}


int main() {
    int arr[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int length = sizeof(arr)/sizeof(arr[0]);

    sort(arr, length);

    for (int i = 0; i < length; ++i) {
        cout << arr[i] << " ";
    }

    return 0;
}