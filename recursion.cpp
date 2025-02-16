#include<iostream>
using namespace std;

int fibonacci(int n) {
    if (n == 1 || n == 2)
        return 1;
    return (fibonacci(n-1) + fibonacci(n-2));
}

int sumOfArray(int *arr,int start, int n) {
    if (n == 0)
        return 0;
    if (start == n-1)
        return arr[start];
    return (arr[start] + sumOfArray(arr, start+1, n));
}

bool numberInArray(int arr[], int n, int x, int start) {
    if (start == n)
        return false;
    if (arr[start] == x)    
        return true;
    return numberInArray(arr, n, x, start+1);
}

int tripletSum(int arr[], int n, int num) {
    int count {};

    for(int i = 0; i < n; ++i) {
        for(int j = i+1; j < n; ++j) {
            pair<int, int> p1 = make_pair(arr[i], arr[j]);
            int temp = p1.first + p1.second;
            for(int k = j+1; k < n; ++k) {
                if (num-temp == arr[k]) {
                    count++;
                    cout << p1.first << " " << p1.second << " " << arr[k] << endl;
                }
            }
        }
    }

    return count;
}

int main() {
    int n, x;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    cin >> x;

    // cout << fibonacci(n) << endl;
    // cout << sumOfArray(arr,0, n) << endl;
    // numberInArray(arr, n, x, 0) ? cout << "True\n" : cout << "False\n";
    cout << tripletSum(arr, n, x) << endl;

    return 0;
}