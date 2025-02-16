#include<iostream>
using namespace std;
 
template <class T>
class vector {

    public:
    T *arr;
    int size;

    vector(int m) {
        size = m;
        arr = new T[size];
    }

    T dotProduct(vector &v) {
        T d = 0;

        for (int i = 0; i < size; ++i) {
            d += this->arr[i] * v.arr[i];
        }

        return d;
    }
};

int main() {
    // vector<int> v1(3);
    // v1.arr[0] = 3;
    // v1.arr[1] = 4;
    // v1.arr[2] = 5;
    // vector<int> v2(3);
    // v2.arr[0] = 8;
    // v2.arr[1] = 7;
    // v2.arr[2] = 6;
    // int a = v1.dotProduct(v2);
    // cout << a << endl;

    vector<float> v1(3);
    v1.arr[0] = 3.3;
    v1.arr[1] = 4.6;
    v1.arr[2] = 5.2;
    vector<float> v2(3);
    v2.arr[0] = 8.1;
    v2.arr[1] = 7.9;
    v2.arr[2] = 6.4;
    float a = v1.dotProduct(v2);
    cout << a << endl;

    return 0;
}