#include<iostream>
#include<stack>
using namespace std;

bool balancedParanthesis(string str, int len) {
    stack<char> s;

    for (int i = 0; i < len; ++i) {
        if(str[i] == '(' || str[i] == '{' || str[i] == '[' ) {
            s.push(str[i]);
        } 

        if (str[i] == ')') {
            if(s.top() == '(') {
                s.pop();
            }else {
                return false;
            }
        }
        
        if (str[i] == '}') {
            if(s.top() == '{') {
                s.pop();
            } else {
                return false;
            }
        }

        if (str[i] == ']') {
            if(s.top() == '[') {
                s.pop();
            } else {
                return false;
            }
        }

    }

    return s.empty();
}

void reverseStack(stack<int> &s1, stack<int> &s2) {

    while(!s1.empty()) {
        s2.push(s1.top());
        s1.pop();
    }

    s1 = move(s2);
}

void insertAtBottom(stack<int> &s, int ele) {
    if(s.empty()) {
        s.push(ele);
        return;
    }

    int topEle = s.top();
    s.pop();
    insertAtBottom(s, ele);
    s.push(topEle);
}

void reverse(stack<int> &s) {
    if(s.empty()) 
        return;

    int ele = s.top();
    s.pop();
    reverse(s);
    insertAtBottom(s, ele);
}

int main() {
    string str;
    // cin >> str;
    stack<int> s1;
    stack<int> s2;

    s1.push(2);
    s1.push(8);
    s1.push(15);
    s1.push(1);
    s1.push(10);

    // cout << balancedParanthesis(str, str.length()) << endl;
    // reverseStack(s1, s2);
    reverse(s1);

    while(!s1.empty()) {
        cout << s1.top() << " ";
        s1.pop();
    }
    cout << endl;

    // while(!s2.empty()) {
    //     cout << s2.top() << " ";
    //     s2.pop();
    // }
    // cout << endl;

    return 0;
}