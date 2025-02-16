#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(false);\
            cin.tie(NULL);
#define ll long long int


int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    string input, output;
    getline(cin, input);

    for (int i = 0; i < input.length(); i++)
    {
        
    cout << isupper(input[i])<< " ";
        
    }
    
    
    


    return 0;
}