#include<iostream>
#include"pair.cpp"
using namespace std;

int main() {
    Pair<int, int> p1;

    p1.setX(10);
    p1.setY(10);
    cout << p1.getX() << " " << p1.getY() << endl;

    Pair<int, double> p2;

    p2.setX(10);
    p2.setY(10.5);
    cout << p2.getX() << " " << p2.getY() << endl;

    Pair<Pair<int, int>, int> p3;

    p3.setY(10);
    Pair<int, int> p4;
    p4.setX(15);
    p4.setY(20);

    p3.setX(p4);

    cout << p3.getX().getX() << " " << p3.getX().getY() << " " << p3.getY() << endl;

    return 0;
}