#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(false);\
            cin.tie(NULL);
#define ll long long int

vector<int> stateOfCells (vector<int> cell, int days) {
    vector<int> answer(8, 0);

    for (int j = 0; j < days; ++j) {
        for (int i = 0; i < 8; ++i) {
            if (i == 0) {
                if (cell[1] == 0) answer[0] = 0;
                else answer[0] = 1;
            }

            else if (i == 7) {
                if (cell[6] == 0) answer[i] = 0;
                else answer[i] = 1;
            } else {
                
                if (cell[i-1] == cell[i+1]) answer[i] = 0;
                else  answer[i] = 1;
            }
        }
    }

    return answer;   
}

int main() {
    vector<int> cell {1, 0, 0, 0, 0, 1, 0, 0};
    vector<int> answer;
    answer = stateOfCells(cell, 1);

    for (auto x: answer) {
        cout << x << " ";
    }
    cout << endl;

    // for (int i = 0; i < 7; ++i) {
    //     if (cell[i+1] == 0) cout << "yo  ";
    // }
    

    return 0;
}