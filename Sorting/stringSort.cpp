#include<iostream>
#include<algorithm>
using namespace std;

int main() {
    int n;
    string a, str;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> a;
        str += a;
    }

    cout << str << endl;
    sort(str.begin(), str.end());
    cout << str << endl;

    return 0;
}