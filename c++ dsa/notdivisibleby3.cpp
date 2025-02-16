#include<bits/stdc++.h>
using namespace std;

void notDivisibleBy3(int arr[], int n) {
    int count0 = count(arr, arr+n, 0);
    int count1 = count(arr, arr+n, 1);
    int count2 = count(arr, arr+n, 2);

    if (count0 <= (count1+count2+1))
        cout << "True\n";
    else 
        cout << "False\n";

}

int main() {
    int arr[] {0, 2, 0, 1, 0, 0};
    int n = sizeof(arr) / sizeof(arr[0]);

    notDivisibleBy3(arr, n);    

    return 0;
}