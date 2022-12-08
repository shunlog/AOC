#include <iostream>
#include <bitset>
#include <numeric>
#include <fstream>
#include <map>
#define FN "in.txt"
#define N 36

using namespace std;
using ull = unsigned long long;

int main(int argc, char *argv[]) {
    ifstream f(FN);
    string line, arg, mask;

    map<int,bitset<N>> mem;

    while(getline(f,line)){
        if(line.substr(0,4) == "mask"){
            mask = line.substr(line.find('=')+2);
        } else {
            uint s = line.find('[');
            uint l = line.find(']');
            ull addr = stoi(line.substr(s+1,l-s-1));
            ull val = stoi(line.substr(line.find('=')+2));
            bitset<N> n(val);
            for(uint i = 0; i < mask.size(); i++){
                switch(mask[i]){
                    case '1': n.set(N-i-1,true); break;
                    case '0': n.set(N-i-1,false); break;
                }
            }
            mem[addr] = n;
        }
    }

    ull S = accumulate(mem.begin(), mem.end(), 0,
                       [] (int value, const map<int, bitset<N>>::value_type& p)
                           { return value + p.second.to_ulong(); });
    cout << "Silver: " << S << '\n';

    return 0;
}
