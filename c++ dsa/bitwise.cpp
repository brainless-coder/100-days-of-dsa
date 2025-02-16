#include<iostream>
#include<algorithm>
#include<numeric>
using namespace std;

int uniqueNo(int *arr, int n) {
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        ans ^= arr[i]; 
    }
    return ans;
}

void oddEven(int n) {
    if (n & 1) cout << "Odd\n";
    else cout << "Even\n";
}

void swap(int a, int b) {
    // a = a+b;
    // b = a-b;
    // a = a-b;

    a = a^b;
    b = a^b;
    a = a^b;

    cout << a << " " << b << endl;
}

int setBits(int n) {
    int count {};

    // TC: O(no of bits)
    // while(n > 0) {
    //     count += (n&1);
    //     n >>= 1;
    // }

    // TC: O(no of set bits)
    while(n) {
        count++;
        n &= (n-1); 
    }

    return count;
}

// tell minm no of bits we need to change to convert a -> b
int changeBitsToConvert(int a, int b) {
    int ans = a^b;
    return setBits(ans);
}

int getIthBit(int n, int i) {
    int mask = 1 << i;
    return (n&mask) ? 1 : 0;
}

int setIthBit(int n, int i) {
    int mask = 1 << i;
    n |= mask;
    return getIthBit(n, i);
}

int clearIthBit(int n, int i) {
    int mask = ~(1 << i);
    n &= mask;
    return getIthBit(n, i);
}

void printSubseq(string str, string curr = "", int index = 0) {
    if (index == str.length()) {
        cout << curr << endl;
        return;
    }

    printSubseq(str, curr, index+1);
    printSubseq(str, curr+str[index], index+1);
}

void filterSeq(string a, int n) {
    int i {};
    while(n > 0) {
        (n&1) ? cout << a[i] : cout << "";
        i++;
        n >>= 1;
    }
    cout << endl;
}

void generateSubseq(string a) {
    int n = a.length();
    int range = 1 << n;
    for (int i = 0; i < range; ++i) {
        filterSeq(a, i);
    }
}

int missingNumber(int arr[], int n) {
    // int freq[n+1] {}, ans = 0;

    // for (int i = 0; i < n; ++i) {
    //     freq[arr[i]]++;
    // }

    // for (int i = 0; i < n+1; ++i) {
    //     if (freq[i] == 0) 
    //         ans = i;
    // }

    // int sum = accumulate(arr, arr+n, 0);
    // int totalSum = (n * (n+1)) / 2;
    // int ans = totalSum-sum;

    // Bitwise Approach
    int x {}, y {};
    for (int i = 0; i < n; ++i) {
        x ^= arr[i];
    }

    for (int i = 0; i < n+1; ++i) {
        y ^= i;
    }

    int ans = x^y;

    return ans;
}

void twoUniqueNos(int arr[], int n) {
    int x {}, i {};

    // we will get the XOR of tow unique nos
    for (int i = 0; i < n; ++i) {
        x ^= arr[i];
    }

    // position of setBit of x
    while(x) {
        if (x&i) {
            break;
        } else {
            i++;
            x >>= 1;
        }
    }

    int mask = 1 << i;

    // in the array find the element whose Ith bit is set
    for (int i = 0; i < n; ++i) {
        
    }


}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    // For printing all the subsequences of a string
    // string a;
    // cin >> a;
    // generateSubseq(a);
    // printSubseq(a);


    // for swap fn
    // int a, b;
    // cin >> a >> b;
    // swap(a, b);
    // cout << changeBitsToConvert(a, b) << endl;


    // cout << uniqueNo(arr, n) << endl;
    // oddEven(n);
    // cout << setBits(n) << endl;
    cout << missingNumber(arr, n) << endl;

    // int i;
    // cin >> i;
    // cout << getIthBit(n, i) << endl;
    // cout << setIthBit(n, i) << endl;
    // cout << clearIthBit(n, i) << endl;


    

    return 0;
}