#include<iostream>
#include<unordered_map>
#include<string>
#include<vector>
using namespace std;

int main() {
    unordered_map<string, int> ourMap;

    // Insertion: we can insert in a map using pair or square braces syntax
    // Insertion in 3 ways
    pair<string, int> p("abc", 1);
    ourMap.insert(p);
    ourMap["def"] = 2;
    ourMap["ghi"] = 3;
    ourMap["fgk"] = 5;
    ourMap.insert(make_pair("jkl", 4));

    // finding or accessing an element
    // cout << ourMap.at("abc") << endl;
    // cout << ourMap["def"] << endl;

    // cout << ourMap.at("ghi");   

    // This will create a key-value pair with the default values
    // cout << ourMap["ghi"] << endl;      
    // cout << "size: " << ourMap.size() << endl;

    // check the presence of a key
    // count() fn returns 1 if the element is present otherwise 0
    // cout << ourMap.count("ghi") << endl;

    // We can also use iterators to search for a key in map
    // auto it = ourMap.find("ghi");
    // if (it != ourMap.end()) {
    //     cout << "value of ghi is: " << it->second;
    // } else {
    //     cout << "ghi doesn't exist\n";
    // }

    // Erase a key-value
    // ourMap.erase("ghi");
    // cout << ourMap.count("ghi") << endl;

    // Traversing a map
    // for(auto x: ourMap) {
    //     cout << x.first << " " << x.second;
    //     cout << endl;
    // }

    // Both the auto and pair will work same
    // for(pair<string, int> x: ourMap) {
    //     cout << x.first << " " << x.second;
    //     cout << endl;
    // }

    // Traversing a map using iterator
    // unordered_map<string, int>::iterator it = ourMap.begin();
    // while (it != ourMap.end()) {
    //     cout << it->first << " " << it->second << endl;
    //     it++;
    // }
    // cout << endl;

    // using iterators in the find and erase function
    // unordered_map<string, int>::iterator it1 = ourMap.find("abc");
    // auto it2 = ourMap.find("fgk");
    // ourMap.erase(it1, it2);


    // cout << ourMap.bucket_count() << endl;
    // cout << ourMap.max_bucket_count() << endl;


    // Printing the whole hastable
    for (int i = 0; i < ourMap.bucket_count(); ++i) {
        cout << "Bucket " << i << " ==>";
        for (auto it = ourMap.begin(i); it != ourMap.end(i); it++) {
            cout << it->first << ", " << it->second << "\t";
        }
        cout << endl;
    }

    
    return 0;
}