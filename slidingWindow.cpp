#include<bits/stdc++.h>
using namespace std;

int maxSubArraySumNaive(int *arr, int n, int k) {
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

int maxSubArraySumSlidingWindow1(int *arr, int n, int k) {
    int currSum {}, maxSum {};
    for (int i = 0; i < k; ++i) currSum += arr[i];
    maxSum = currSum;
    
    for (int i = 0, j = k; j < n; i++, j++) {
        currSum += arr[j];
        currSum -= arr[i];
        if (currSum > maxSum)   maxSum = currSum;
    }
    return maxSum;
}

int maxSubArraySumSlidingWindow2(int arr[], int n, int k) {
    int currSum {}, maxSum = -99999;
    for(int i = 0, j = 0; j < n; ++j) {
        currSum += arr[j];
        if (j-i+1 < k)  continue;
        if (j-i+1 == k) {
            maxSum = max(currSum, maxSum);
            currSum -= arr[i];
            i++;
        }
    }
    return maxSum;
}

void firstNegInEveryWindowNaive(int *arr, int n, int k) {
    for (int i = 0; i < n-k+1; ++i) {
        bool flag = false;
        for (int j = i; j < i+k; ++j) {
            if (arr[j] < 0) {
                cout << arr[j] << " ";
                flag = true;
                break;
            }
        }
        if (!flag)  cout << 0 << " ";
    }
    cout << endl;
}

int main() {

    int n, k;
    cin >> n >> k;
    int arr[n];
    for(int i = 0; i < n; ++i)  cin >> arr[i];

    // cout << maxSubArraySumNaive(arr, n, k) << endl;
    // cout << maxSubArraySumSlidingWindow1(arr, n, k) << endl;
    // cout << maxSubArraySumSlidingWindow2(arr, n, k) << endl;
    firstNegInEveryWindowNaive(arr, n, k);

    return 0;
}