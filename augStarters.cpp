#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(false);\
            cin.tie(NULL);
#define ll long long int

void hardestProblemBet() {
    int a, b, c;
    cin >> a >> b >> c;

    if (c < a && c < b) cout << "Alice\n";
    else if (b < a && b < c) cout << "Bob\n";
    else    cout << "Draw\n";
}

void oddRepeat() {
    int n, k, s;
    cin >> n >> k >> s;

    int sum {}, j = 1;
    for (int i = 0; i < n; ++i, j+=2) {
        sum += j;
    }

    int ans = (s-sum) / (k-1);
    cout << ans << endl;
}

void removeOneEle() {
    ll n;
    cin >> n;
    ll a[n], b[n];
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n-1; ++i) cin >> b[i];

    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            if (b[i]-a[j] != b[i]-a[j+1]) {
                continue;
            }
            
        }
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int t;
    cin >> t;

    while(t--) {
        removeOneEle();
    }

    return 0;
}