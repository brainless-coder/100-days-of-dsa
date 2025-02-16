#include<bits/stdc++.h>
using namespace std;

long merge(long int *arr, int l, int mid, int r) {
    int i = l;
    int j = mid + 1;
    long swaps = 0;

    long int temp[1000000], k = 0;

    while ( (i <= mid) && (j <=r) ) {
        if (arr[i] <= arr[j]) {
            temp[k] = arr[i++];
        }
        else {
            temp[k] = arr[j++];
            swaps += (mid - i + 1);
        }
        k++;
    }

    while (i <= mid) {
        temp[k++] = arr[i++];
    }
     
    while (j <= r) {
        temp[k++] = arr[j++];
    }

    for (int m = l, p = 0; m <= r; ++m, ++p) {
        arr[m] = temp[p];
    }

    return swaps;
}


long merge_solution (long int arr[], int l, int r) {
    long count = 0;

    if (r > l) {
        int mid = l + (r-l) / 2;

        count += merge_solution(arr, l, mid);
        count += merge_solution(arr, mid+1, r);

        count += merge(arr, l, mid, r);
    }

    return count;
}


int main() {
    // for fast I/O
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);   

    int t;
    unsigned int n;
    cin >> t;

    while (t--) {
        cin >> n;
        long int arr[n];
        long inv = 0;

        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }    

        inv = merge_solution(arr, 0, n-1);
        cout << inv << "\n";
    }

    return 0;
}