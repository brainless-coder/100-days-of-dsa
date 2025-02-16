#include<iostream>
using namespace std;

void printMatrix(int mat[][10], int r, int c) {
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

void printSnakePattern(int mat[][10], int r, int c) {
    for (int i = 0; i < r; ++i) {
        if (i%2 == 0) {
            for (int j = 0; j < c; ++j) {
                cout << mat[i][j] << " ";
            }
        } else {
            for (int j = c-1; j >= 0; --j) {
                cout << mat[i][j] << " ";
            }
        }
        cout << endl;
    }
}

void transpose(int mat[][10], int r, int c) {
    for (int i = 0; i < r; ++i) {
        for (int j = i+1; j < c; ++j) {
            swap(mat[i][j], mat[j][i]);
        }
    }

}

void rotate(int mat[][10], int r, int c) {
    // for (int i = c-1; i >= 0; --i) {  
    //     for (int j = 0; i < r; ++j) {  
    //         cout << mat[j][i] << " ";
    //     }
    //     cout << endl;
    // }

    transpose(mat, r, c);

    for (int i = 0; i < r/2; ++i) {
        for (int j = 0; j < c; ++j) {
            swap(mat[i][j], mat[r-1-i][j]);
        }
    }    


}

void searchEle(int mat[][10], int r, int c, int x) {
    int p = -1, q = -1;

    for (int i = 0; i < r; ) {
        for (int j = c-1; j >= 0; ) {
            if (mat[i][j] < x) {
                i++;
            } else if (mat[i][j] > x) {
                j--;
            } else if (mat[i][j] == x) {
                p = i; 
                q = j;
                break;
            }
        }
        if (p != -1) {
            break;
        }
    }

    cout << p << q << endl;

}

void boundaryTraversal(int mat[][10], int r, int c) {
    int i, j;

    i = 0;
    for (j = 0; j < c; ++j) {
        cout << mat[i][j] << " ";
    }

    j = c-1;
    for (i = 1; i < r; ++i) {
        cout << mat[i][j] << " ";
    }

    i = r-1;
    for (j = c-2; j >= 0; --j) {
        cout << mat[i][j] << " ";
    }

    j = 0;
    for (i = r-2; i >= 0; --i) {
        cout << mat[i][j] << " ";
    }
}

void spiralTraversal(int mat[][10], int r, int c) {
    int top {}, left {}, dirn {}, bottom = r-1, right = c-1;

    while(top <= bottom && left <= right) {
        if (dirn == 0) {
            for (int i = left; i <= right; ++i) 
                cout << mat[top][i] << " ";
            top++;
        } else if (dirn == 1) {
            for (int i = top; i <= bottom; ++i) 
                cout << mat[i][right] << " ";
            right--;
        } else if (dirn == 2) {
            for (int i = right; i >= left; --i)
                cout << mat[bottom][i] << " ";
            bottom--;
        } else if (dirn == 3) {
            for (int i = bottom; i >= top; --i)
                cout << mat[i][left] << " ";
            left++;
        }

        dirn = (dirn+1) % 4;
    }

}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif  

    int r, c;
    cin >> r >> c;
    int mat[10][10];

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> mat[i][j];
        }
    }

    // printMatrix(mat, r, c);
    // printSnakePattern(mat, r, c);
    // transpose(mat, r, c);
    // rotate(mat, r, c);
    // printMatrix(mat, r, c);
    // searchEle(mat, r, c, 3);
    // boundaryTraversal(mat, r, c);
    spiralTraversal(mat, r, c);

    return 0;
}