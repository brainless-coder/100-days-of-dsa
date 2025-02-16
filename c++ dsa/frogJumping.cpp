#include<iostream>
#include<algorithm>
#include<numeric>
using namespace std;

void frogJumps(int *dist, int n, int k) {
    int currPos {}, jumps{};

    while (currPos < n) {
        if (dist[currPos] > k) {
            cout << "NO" << endl;
            return;
        } else  {
            jumps++;
            int distJumped {};
            while (currPos < n && (distJumped + dist[currPos]) <= k) {
                distJumped += dist[currPos];
                currPos++;
            }
        }
    }

    cout << jumps << endl;
}

int main() {
    int n, k;
    cin >> n >> k;
    int dist[n+1];

    for (int i = 0; i <= n; ++i) {
        cin >> dist[i];
    }

    frogJumps(dist, n+1, k);

    return 0;
}