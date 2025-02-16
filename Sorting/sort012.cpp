#include<iostream>
using namespace std;

void naiveSoln(int arr[], int n) {
    int count0 {}, count1 {}, count2 {};

    for (int i = 0; i < n; ++i) {
        if (arr[i] == 0)
            count0++;
        else if (arr[i] == 1)
            count1++;
        else 
            count2++;
    }    

    int i = 0;

    while(count0 > 0) {
        arr[i++] = 0;
        count0--;
    }

    while(count1 > 0) {
        arr[i++] = 1;
        count1--;
    }

    while(count2 > 0) {
        arr[i++] = 2;
        count2--;
    }
}

void optimizedApproach(int arr[], int n) {
    int low = 0, high = n-1, mid = 0;

    while (mid <= high) {
        switch (arr[mid]) {
        case 0:
            swap(arr[mid++], arr[low++]);
            break;
        case 1:
            mid++;
            break;
        case 2:
            swap(arr[mid], arr[high--]);
            break;
        }
    }
    
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] {0, 1, 2, 2, 1, 2, 1 , 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // naiveSoln(arr, n);
    optimizedApproach(arr, n);
    printArray(arr, n);
    
    return 0;
}