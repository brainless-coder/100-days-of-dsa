#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(false);\
            cin.tie(NULL);
#define ll long long int

void anagramNaive() {
    string str1, str2;
    getline(cin, str1);
    getline(cin, str2);

    int n1 = str1.length();
    int n2 = str2.length();

    if (n1 != n2) {
        cout << "Not a anagram\n";
        return;
    }

    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());

    for (int i = 0; i < n1; ++i) {
        if (str1[i] != str2[i]) {
            cout << "Not an anagram\n";
            return;
        }
    }

    cout << "Anagram\n";
}

void anagramOptimized() {
    string s1, s2;
    getline(cin, s1);
    getline(cin, s2);

    int n1 = s1.length();
    int n2 = s2.length();

    if (n1 != n2) {
        cout << "Not an anagram\n";
        return;
    }

    // int count[256] {};
    array<int, 256> count {};
    // array<int, 256> count1 {};
    // array<int, 256> count2 {};

    for (int i = 0; i < n1; ++i) {
        count[s1[i]]++;
    }

    for (int i = 0; i < n2; ++i) {
        count[s2[i]]--;
    }

    // if (equal(begin(count1), end(count1), begin(count2))) {
    //     cout << "Anagram\n";
    // } else {
    //     cout << "Not an Anagram\n";
    // }

    for (auto x: count) {
        if (x != 0) {
            cout << "Not an Anagram\n";
            return;
        }
    }

    cout << "Anagram\n";

}

int firstRepeatingChar() {
    string str;
    int res = INT_MAX;
    getline(cin, str);
    int n = str.length();

    array<int, 256> count;
    count.fill(-1);

    for (int i = 0; i < n; ++i) {
        if (count[str[i]] == -1)
            count[str[i]] = i;
        else 
            res = min(res, count[str[i]]);
    }

    if (res > n) 
        res = -1;

    return res;

}

char firstNonRepeating() {
    string str;
    getline(cin, str);
    int n = str.length();

    array<int, 256> count {};

    for (auto x: str) {
        count[x]++;
    }

    for (auto x: str) {
        if (count[x] == 1)
            return x;
    }

}

int firstNonRepeatingusingPairs() {
    string str;
    int res = INT_MAX;
    getline(cin, str);
    int n = str.length();

    pair<int , int> arr[256] {};

    for (int i = 0; i < n; ++i) {
        arr[str[i]].first++;
        arr[str[i]].second = i;
    }

    for (int i = 0; i < 256; ++i) {
        if (arr[i].first == 1) {
            res = min(res, arr[i].second);
        }
    }

    return res;
}

int factorial(int n) {
    return (n == 0 || n == 1) ? 1 : n * factorial(n-1);
}

int smallerinRight(string a, int low, int high) {
    int count {};

    for (int i = low+1; i <= high; ++i) {
        if (a[i] < a[low])
            count++;
    }

    return count;
}

int lexographicRank() {
    string str;
    getline(cin, str);
    int n = str.length();
    int rank = 1;

   
    for (int i = 0; i < n; ++i) {
        int countRight = smallerinRight(str, i, n-1);
        int mul = factorial(n-1-i);

        // cout << countRight << " " << mul << endl;
        rank += (mul*countRight);
    }

    return rank;

}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    // anagramNaive();
    // anagramOptimized();
    // cout << firstRepeatingChar() << endl;
    // cout << firstNonRepeating() << endl;
    // cout << firstNonRepeatingusingPairs() << endl;
    cout << lexographicRank() << endl;
    
    return 0;
}