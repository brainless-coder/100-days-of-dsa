#include<bits/stdc++.h>
using namespace std;

void zeroPairSum(int arr[], int size) {
    unordered_set<int> zeroPair;
    vector<pair<int, int>> ans {};

    for(int i = 0; i < size; ++i) {
        zeroPair.insert(arr[i]);
    }

    for (int i = 0; i < size; ++i) {
        if (arr[i] > 0) {
            if (zeroPair.count((-arr[i])) != 0) {
                ans.push_back(make_pair(arr[i], (-arr[i])));
            }
        }
    }

    for (auto it: ans) {
        cout << it.first << " " << it.second << endl;
    }
}

// vector<int> removeDuplicates(int *arr, int size) {
//     vector<int> output {};
//     unordered_map<int, bool> seen;

//     for (int i = 0; i < size; ++i) {
//         if (seen.count(arr[i]) > 0) {
//             continue;
//         }
//         seen[arr[i]] = true;
//         output.push_back(arr[i]);
//     }

//     return output;
// }

void removeDuplicates(int arr[], int size) {
    unordered_set<int> seen;

    for (int i = 0; i < size; ++i) {
        seen.insert(arr[i]);
    }

    for(auto it: seen) {
        cout << it << " ";
    }
    cout << endl;
}

int maxmFrequency(int *arr, int n) {
    map<int, int> freq;

    for (int i = 0; i < n; ++i) {
        freq[arr[i]]++;
    }

    int maxm = INT_MIN;
    int ans {};
    for (auto x: freq) {
        maxm = max(x.second, maxm);
        if (maxm == x.second)
            ans = x.first;
    }

    return maxm;
}

void unionIntersection(int arr1[], int arr2[], int n, int m) {
    unordered_set<int> unionAns;
    unordered_set<int> intersectionAns;

    for (int i = 0; i < n; ++i) {
        unionAns.insert(arr1[i]);
    }

    for (int i = 0; i < m; ++i) {
        unionAns.insert(arr2[i]);
    }

    for (auto x: unionAns) {
        cout << x << " ";
    }
    cout << endl;

    for (int i = 0; i < n; ++i) {
        intersectionAns.insert(arr1[i]);
    }

    for (int i = 0; i < m; ++i) {
        if (intersectionAns.count(arr2[i]) > 0) {
            cout << arr2[i] << " ";
        }
    }
    cout << endl;
}


int main() {
    int arr[] {1, 2, 3, 4, 6, 2, 3, 1, 7, 5, 9, 3, 2};
    // int arr[] {1, 2, 3, 4, 5, 6 ,-4, -2, -7, -1};
    int arr1[] {1, 3, 2, 5, 7};
    int arr2[] {2, 5, 6, 9, 11};
    int size = sizeof(arr) / sizeof(arr[0]);
    int n = sizeof(arr1) / sizeof(arr1[0]);
    int m = sizeof(arr2) / sizeof(arr2[0]);

    // vector<int> output = removeDuplicates(arr, size);
    // removeDuplicates(arr, size);
    unionIntersection(arr1, arr2, n, m);

    // for (auto x: output) {
    //     cout << x << " ";
    // }
    // cout << endl;

    // cout << maxmFrequency(arr, size);
    // zeroPairSum(arr, size);

    return 0;
}
