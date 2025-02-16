#include<iostream>
#include<queue>
using namespace std;
#include "queueUsingArray.h"
#include "queueUsingLL.h"

int main() {
    // QueueUsingArray<char> q;

    // q.enqueue(101);
    // q.enqueue(102);
    // q.enqueue(103);
    // q.enqueue(104);
    // q.enqueue(105);
    // q.enqueue(106);

    // cout << q.front() << endl;
    // cout << q.dequeue() << endl;
    // cout << q.dequeue() << endl;
    // cout << q.dequeue() << endl;

    // cout << q.getSize() << endl;
    // cout << q.isEmpty() << endl;
    // cout << q.front() << endl;

    // q.enqueue(107);
    // q.enqueue(108);
    // q.enqueue(109);

    // cout << q.getSize() << endl;
    // cout << q.isEmpty() << endl;
    // cout << q.front() << endl;

    // cout << q.dequeue() << endl;
    // cout << q.front() << endl;


    // QueueUsingLL<int> q;

    // q.enqueue(101);
    // q.enqueue(102);
    // q.enqueue(103);
    // q.enqueue(104);
    // q.enqueue(105);
    // q.enqueue(106);

    // cout << q.front() << endl;
    // cout << q.dequeue() << endl;
    // cout << q.dequeue() << endl;
    // cout << q.dequeue() << endl;

    // cout << q.getSize() << endl;
    // cout << q.isEmpty() << endl;
    // cout << q.front() << endl;

    // q.enqueue(107);
    // q.enqueue(108);
    // q.enqueue(109);

    // cout << q.getSize() << endl;
    // cout << q.isEmpty() << endl;
    // cout << q.front() << endl;

    // cout << q.dequeue() << endl;
    // cout << q.front() << endl;

    // while(!q.isEmpty()) {
    //     cout << q.dequeue() << endl;
    // }
    
    // cout << q.getSize() << endl;
    // cout << q.dequeue() << endl;

    queue<int> q;

    q.push(10);
    q.push(20);
    q.push(30);
    q.push(40);
    q.push(50);

    cout << q.size() << endl;
    cout << q.front() << endl;
    q.pop();
    cout << q.front() << endl;
    cout << q.empty() << endl;

    while(!q.empty()) {
        cout << q.front()<< endl;
        q.pop();
    }

    cout << q.size() << endl;
    cout << q.front() << endl;

    return 0;
}