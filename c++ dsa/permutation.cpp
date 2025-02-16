#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(false);\
            cin.tie(NULL);
#define ll long long int

void permute(string a, int l, int r) {

    if (l == r) {
        cout << a << endl;
        return;
    } else {

        for (int i = l; i <= r; ++i) {
            swap(a[l], a[i]);
            sort(a.begin()+(l+1), a.end());     // for lexographic order
            permute(a, l+1, r);
            swap(a[l], a[i]);
        }
    }
}


int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    string str;
    getline(cin, str);
    int n = str.length();
    int rank = 1;
    string input = str;

    sort(str.begin(), str.end());       // for lexographic order
    permute(str, 0, n-1);

    return 0;
}