#include<iostream>
#include<limits>
using namespace std;

void countingSort(int *arr, int n) {
    int output[n] {};
    int max = numeric_limits<int>::min();

    // For finding the maxm element  
    // O(n)
    for (int i = 0; i < n; ++i) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    int temp[max+1] {};
    
    // storing frequencies in the Auxiliary array
    // O(n)
    for (int i = 0; i < n; ++i) {
        ++temp[arr[i]];
    }

    // making cummulataive frequency array
    // O(max)
    for (int i = 1; i < max+1; ++i) {
        temp[i] += temp[i-1];
    }

    // for sorting the elements
    // O(n)
    for (int i = n-1; i >= 0; i--) {
        output[--temp[arr[i]]] = arr[i];
    }

    // copying values back to the original array
    // O(n)
    for (int i = 0; i < n; ++i) {
        arr[i] = output[i];
    }

}

int main() {
    int arr[] {5, 2, 9, 5, 2, 3, 5};
    int len = sizeof(arr) / sizeof(arr[0]);

    countingSort(arr, len);

    for (int i = 0; i < len; ++i) {
        cout << arr[i] << " ";
    }

    return 0;
}