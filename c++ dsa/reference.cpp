#include<iostream>
using namespace std;

int main() {
    int x = 10;
    int &y = x;

    cout << x << " " << y << endl;
    x += 5;
    cout << x << " " << y << endl;
    y = x + 10;
    cout << x << " " << y << endl;

    return 0;
}