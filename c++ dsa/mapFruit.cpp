#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;

class Fruit {
    public:
        string name;
        int price;
        string city;

        Fruit() {

        }

        Fruit(string name, int price, string city) {
            this->name = name;
            this->price = price;
            this->city = city;
        }
};

int main() {
    unordered_map<string, Fruit> myMap;
    Fruit f("Mango", 100, "Patna");
    Fruit f1("Apple", 150, "Delhi");

    myMap[f.name] = f;
    myMap[f1.name] = f1;
    cout << myMap["Apple"].city << endl;

    Fruit fs = myMap["Mango"];
    // cout << fs.city<< endl;
    // cout << fs.price<< endl;
    // cout << fs.name<< endl;

    // cout << myMap.count("Apple") << endl; 

    // string fruit;
    // cout << "Enter a fruit to search: ";
    // cin >> fruit;

    // if (myMap.count(fruit) != 0) {
    //     cout << "Price is " << myMap[fruit].price << endl;
    // } else {
    //     cout << "Fruit doesn't exist.\n";
    // }
}