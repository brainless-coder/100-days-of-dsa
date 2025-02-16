#include<iostream>
#include<vector>
using namespace std;

int main() {
    int l[] {1, 2, 5, 15};
    int r[] {5, 8, 7, 18};
    int n = sizeof(l) / sizeof(l[0]);
    vector<int> vect(1000);

    for (int i = 0; i < n; ++i) {
        vect[l[i]]++;
        vect[r[i]+1]--;
    }

    int maxm = vect[0], res {};
    for (int i = 1; i < 1000; ++i) {
        vect[i] += vect[i-1];

        if (vect[i] > maxm) {
            maxm = vect[i];
            res = i;
        }
    }

    cout << res << " occured " << maxm << " times\n";

    return 0;
}