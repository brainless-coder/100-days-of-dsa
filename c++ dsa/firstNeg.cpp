#include<iostream>
#include<vector>
using namespace std;

void naiveApproach(int arr[], int n, int k) {
    for (int i = 0; i < n-2; ++i) {
        for (int j = i; j < i+3; ++j) {
            if(arr[j] < 0) {
                cout << arr[j] << " ";
                break;
            } else if (j == i+2) {
                cout << 0 << " ";
            }
        }
    }
    cout << endl;
}

void slidingApproach(int arr[], int n, int k) {
    int i {}, j {};
    vector<int> vect;

    while (j < n) {
        if (arr[j] < 0) {
            vect.push_back(arr[j]);
        }

        if (j-i+1 < k) {
            j++;
        } else if (j-i+1 == k) {
            if (vect.size() == 0) {
                cout << 0 << " ";
            } else {
                cout << vect[0] << " ";
            }

            if (arr[i] < 0) {
                vect.erase(vect.begin());
            }

            i++;
            j++;   
        }
    }
    cout << endl;
}

int main() {
    int arr[] {12, -1, -7, 8, -15, 30, 13, 28, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;

    // naiveApproach(arr, n, k);
    slidingApproach(arr, n, k);

    return 0;
}