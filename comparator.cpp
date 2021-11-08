#include<bits/stdc++.h>
using namespace std;

bool should_i_swap(int a, int b) {
    if(a < b)   return true;
    return false;
}

bool should_i_swap(pair<int,int> a, pair<int,int> b) {
    if (a.first != b.first) {
        if (a.first > b.first)   return true;
        return false;
    } else {
        if (a.second < b.second)    return true;
        return false;
    }
}

// comparator me whi return karwado, jis order me haame final sorted array chahiye
bool cmp(pair<int,int> a, pair<int,int> b) {
    if (a.first != b.first) {
        return a.first < b.first;
    } 
    return a.second > b.second;
}

int main() {
    // vector<int> a {56, 34, 23, 2, 55, 32, 8};
    vector<pair<int,int>> a {{2, 5}, {5, 3}, {5, 5}, {7, 8}, {9, 2}, {9, 6}, {1, 5}};
    int n = a.size();

    // Custom logic of sort in O(n^2)
    // for(int i = 0; i < n; ++i) {
    //     for(int j = i+1; j < n; ++j) {
    //         if(should_i_swap(a[i], a[j])) {
    //             swap(a[i], a[j]);
    //         }
    //     }
    // }

    sort(a.begin(), a.end(), cmp);
    
    for(int i = 0; i < n; ++i) {
        cout << a[i].first << " " << a[i].second << endl;
    }

    return 0;
}