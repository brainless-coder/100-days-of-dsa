#include<iostream>
using namespace std;

int main() {
    int x;
    cin >> x;

    int l = 0, r = x;

    while (l <= r) {
        int mid = l + (r-l) / 2;

        if (mid*mid > x) {
            r = mid-1;
        } else if (mid*mid < x) {
            l = mid+1;
        } else if (mid*mid == x) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";

    return 0;
}