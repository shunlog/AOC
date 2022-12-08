#include <iostream>
#include <fstream>
#include <vector>
#define FN "in.txt"

using namespace std;
using ll = long long;

ll part1(vector<int> &, int);

int main(int argc, char *argv[]) {
    ifstream f(FN);
    string s;
    getline(f,s);
    int t0 = stoi(s);
    vector<int> busses;
    while(getline(f,s,',')){
        if(s != "x")
            busses.push_back(stoi(s));
    }

    // cout << t0 << '\n';
    // for (auto i: busses) {
    //     cout << i << '\n';
    // }

    cout << "Silver: " << part1(busses, t0);

    return 0;
}

ll part1(vector<int> &busses, int t0){
    int sol = 0;
    int min=((uint)~0)>>1;
    for(int x:busses){
        if(x - (t0 % x) < min){
            min = x - (t0 % x);
            sol = x;
        }
    }

    return (sol - (t0 % sol)) * sol;
}
