#include<iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    // int arr[n];
    
    // making a dynamic array using the new keyword
    // arr stores the address of the 1st ele of the dynamic array
    // same jaise normal arrays me hota h
    int *arr = new int[n];      

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // whenever we use new keyword, we should use delete
    // otherwise memory bhar jaayegi
    delete [] arr;
    arr = NULL;

    return 0;
}