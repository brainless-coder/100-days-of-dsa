#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(false);\
            cin.tie(NULL);
#define ll long long int

void oneInBinaryArray() {
    // given a binary array, divide it in 3 parts 
    // s.t each part has equal number of ones
    // the three partitions may or may not be equal

    int arr[] {0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0};
    int n = sizeof(arr)/sizeof(arr[0]);

    int count1 = count(arr, arr+n, 1);

    if (count1%3 == 0) {
        cout << "True\n";

        int x = count1 / 3;
        int part {};

        for (int i = 0; i < n; ++i) {
            cout << arr[i] << " ";
            if (arr[i] == 1) {
                x--;
            }

            if (x == 0) {
                part++;

                if (part < 3) {
                    cout << endl;
                    x = count1/3;
                }
            }
        }
    } else {
        cout << "False\n";
    }

}

void equal3parts() {
    // Same last quest but the 3 partitions should be equal

    // int arr[] {0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0};
    int arr[] {0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0};
    int n = sizeof(arr)/sizeof(arr[0]);

    int count1 = count(arr, arr+n, 1);
    
    if (count1%3 == 0) {
        int one = count1/3;
        int trailingZero {};

        for (int i = n-1; one > 0; --i) {
            if (arr[i] == 0) {
                trailingZero++;
            }

            if (arr[i] == 1) {
                one--;
            }
        }

        // cout << trailingZero << " " << one;
        int zero = trailingZero;
        one = count1/3;
        for (int i = 0; i < n; ++i) {
            cout << arr[i] << " ";

            if (arr[i] == 1) {
                one--;
            }

            if (arr[i] == 0 && one < (count1/3)) {
                zero--;
            }

            if (one == 0 && zero == 0) {
                cout << endl;
                zero = trailingZero;
                one = count1/3;
            }
        }

    } else {
        cout << "The array cannot be divided\n";
    }

}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    // oneInBinaryArray();
    equal3parts();

    return 0;
}