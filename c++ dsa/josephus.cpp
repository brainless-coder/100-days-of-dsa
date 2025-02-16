#include<iostream>
#include<vector>
using namespace std;

int jos(int n, int k) {
    if (n == 1)
        return n;

    return (jos(n-1, k) + k-1) % n+1;
}

int main() {
    int n, k;
    vector<int> vect;
    vector<int>:: iterator it;
    cin >> n >> k;

    cout << jos(n, k);


    return 0;
}