#include<iostream>
using namespace std;

void merge(int arr[], int l, int mid, int r) {
    int i = l;
    int j = mid + 1;

    int temp[r], k  = 0;

    while (i <= mid && j <= r) {
        if (arr[i] <= arr[j]) 
            temp[k] = arr[i++];
        else 
            temp[k] = arr[j++];

        k++;
    }

    while (i <= mid) {
        temp[k] = arr[i++];
        k++;
    }
     
    while (j <= r) {
        temp[k] = arr[j++];
        k++;
    }

    for (int m = l, p = 0; m <= r; m++, p++) {
        arr[m] = temp[p];
    }

}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int mid = (l + (r - l)) / 2;

        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);

        merge(arr, l, mid, r);
    }
}

int main() {
    int arr[] {6, 1, 3, 6, 8, 9, 0, 2, 32, 2, 67, -23, -6};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    mergeSort(arr, 0, len-1);

    for (int i = 0; i < len; ++i) {
        cout << arr[i] << " ";
    }

    return 0;
}