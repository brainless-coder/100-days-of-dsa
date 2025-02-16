#include<iostream>
using namespace std;

void sort(int arr[], int length) {
    int temp;

    for (int i = 0; i < length-1; ++i) {
        for (int j = 0; j < (length-i-1); ++j) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void optimizedSort (int arr[], int length) {
    int temp;
    bool swap;

    for (int i = 0; i < length-1; ++i) {
        swap = false;

        for (int j = 0; j < (length-i-1); ++j) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;

                swap = true;
            }
        }

        if (swap == false)   break;
    }
}

int main() {
    int arr[] {9, 8, 7, 6, 5, 4, 3, 2, 1};
    int length = sizeof(arr)/sizeof(arr[0]);

    sort(arr, length);

    for (int i = 0; i < length; ++i) {
        cout << arr[i] << " ";
    }

    return 0;
}