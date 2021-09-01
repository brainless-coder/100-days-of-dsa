#include<iostream>
using namespace std;

int maxSumNaive(int *arr, int n, int k) {
    int sum {}, ans = -99999;
    for (int i = 0; i < n-k+1; ++i) {
        sum = 0;
        for (int j = i; j < i+k; ++j) {
            sum += arr[j];
        }
        if (sum > ans)  ans = sum;
    }

    return ans;
}

int main() {

    int n, k;
    cin >> n >> k;
    int arr[n];
    for(int i = 0; i < n; ++i)  cin >> arr[i];

    cout << maxSumNaive(arr, n, k) << endl;

    return 0;
}