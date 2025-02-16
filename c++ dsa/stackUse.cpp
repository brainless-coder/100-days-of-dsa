#include<iostream>
#include<stack>
using namespace std;
#include"stackUsingArrays.h"
#include"stackUsingLL.h"

int main() {

    // stack<int> s2;

    // s2.push(10);
    // s2.push(20);
    // s2.push(30);
    // s2.push(40);
    // s2.push(50);

    // cout << s2.top() << endl;
    // s2.pop();
    // cout << s2.top() << endl;

    // cout << s2.size() << endl;
    // cout << s2.empty() << endl;

    
    
    // StackUsingArray<int> s;

    // cout << s.top() << endl;

    // s.push(100);
    // s.push(101);
    // s.push(102);
    // s.push(103);
    // s.push(105);
    // s.push(106);
    // s.push(107);
    // s.push(108);
    // s.push(109);
    // s.push(110);

    // cout << s.top() << endl;

    // cout << s.pop() << endl;
    // cout << s.pop() << endl;
    // cout << s.pop() << endl;

    // cout << s.size() << endl;
    // cout << s.isEmpty() << endl;

    // s.push(10);
    // s.push(20);
    // s.push(30);
    // s.push(40);
    // s.push(50);
    


    StackUsingLL<float> s;

    cout << s.top() << endl;

    s.push(100.34);
    s.push(101.34);
    s.push(102.34);
    s.push(103.34);
    s.push(104.34);

    cout << s.top() << endl;

    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;

    cout << s.size() << endl;
    cout << s.isEmpty() << endl;


    return 0;
}