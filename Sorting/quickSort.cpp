#include<iostream>
#include<cstdlib>
using namespace std;

int partition (int arr[], int low, int high) {
    // int pivot = arr[high];
    int random = rand() % (high - low ) + low;
    int pivot = arr[random];
    swap(arr[random], arr[high]);

    int i = low-1;

    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i+1], arr[high]);

    return (i+1);
}

void quickSort(int arr[], int low, int high) {
    cout << "I am called\n";
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

int main() {
    int arr[] {15, 10 , 12, 13};
    int len = sizeof(arr) / sizeof(arr[0]);

    quickSort(arr, 0, len-1);

    for (int i = 0; i < len; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}