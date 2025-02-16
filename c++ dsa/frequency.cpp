#include<iostream>
#include<vector>
using namespace std;

void frequency_of_all_elements(int arr[], int size) {
    vector<bool> visited (size, false);
    
    for (int i = 0; i < size; ++i) {
        if (visited[i] == true)
            continue;

        int count = 1;
        for (int j = i+1; j < size; ++j) {
            if (arr[i] == arr[j]) {
                count++;
                visited[j] = true;
            }
        }

        cout << arr[i] << ": " << count << endl;
    }
}

void frequency_of_number(int *arr, int size, int x) {
    int count = 0;

    for (int i = 0; i < size; ++i) {
        if (arr[i] == x) 
            count++;
    }

    cout<< count << endl << endl;
} 

int main() {
    int arr[] {5, 6, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 4, 0, 3, 3, 2, 1, 4};
    int size = sizeof(arr)/sizeof(arr[0]);
    int x;

    // cin >> x;
    // frequency_of_number(arr, size, x);
    frequency_of_all_elements(arr, size);

    return 0;
}