#include<iostream>
using namespace std;

void unionArray(int a[], int b[], int n, int m) {
    int ap {}, bp {}, tp {};
    int temp[n+m] {};

    while (ap < n && bp < m) {
        if (a[ap] <= b[bp]) {
            if (temp[tp-1] != a[ap]) 
                temp[tp++] = a[ap];
            ap++;
        } else {
            if (temp[tp-1] != b[bp])
                temp[tp++] = b[bp];
            bp++;
        }
    }

    while (ap < n) {
        if (temp[tp-1] != a[ap]) 
            temp[tp++] = a[ap];
        ap++;    
    }

    while (bp < m) {
        if (temp[tp-1] != b[bp])
            temp[tp++] = b[bp];
        bp++;
    }

    for (int i = 0; i < n+m; ++i) {
        if (temp[i] != 0)
            cout << temp[i] << " ";
    }
    cout << endl;
}

void intersectionArray(int a[], int b[], int n, int m) {
    int ap {}, bp {}, tp {};
    int temp[min(n, m)] {};

    while(ap < n && bp < m) {
        if (a[ap] <= b[bp]) {
            if (a[ap] == b[bp]) {
                temp[tp] = a[ap];
                tp++; 
                ap++;
                bp++;
            } else {
                ap++;
            }
        }
    }

    for (int i = 0; i < min(n, m); ++i) {
        if (temp[i] != 0)
            cout << temp[i] << " ";
    }
    cout << endl;
}

int main() {
    int a[] {5, 15, 20, 25, 30};
    int b[] {15, 20, 30, 45};
    int n = sizeof(a) / sizeof(a[0]);
    int m = sizeof(b) / sizeof(b[0]);

    unionArray(a, b, n, m);
    intersectionArray(a, b, n, m);

        

    return 0;
}