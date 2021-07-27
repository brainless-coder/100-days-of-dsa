#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, q, s;
    cin >> n >> q >> s;
    int actions[q][s];
    for (int i = 0; i < q; ++i) {
        for (int j = 0; j < s; ++j) {
            cin >> actions[i][j];
        }
    }
    int posSoldier;
    cin >> posSoldier;

    int soldiers[n];
    for (int i = 0; i < n; ++i) {
        soldiers[i] = i+1;
    }

    for(int i = 0; i < q; ++i) {
        int row = actions[i][0];
        int col = actions[i][1];

        int rowi, coli;
        for (int j = 0; j < n; ++j) {
            if (soldiers[j] == row) {
                rowi = j;
            } 
            if (soldiers[j] == col) {
                coli = j;
            } 
        }

        while(rowi < coli) {
            swap(soldiers[rowi], soldiers[coli]);
            rowi++;
            coli--;
        }   

    }

    for (int i = 0; i < n; ++i) {
        if (soldiers[i] == posSoldier) {
            cout << i + 1;
        }
    }


    return 0;
}