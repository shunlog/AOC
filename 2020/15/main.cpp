#include <iostream>
#include <sstream>
#include <map>
#define TURNS 30000000
#define log(x) cout << #x << " = " << x << '\n';

using namespace std;

int part1(stringstream &ss){
    string num;
    int curr, prev = -1;
    map<int,int> last_pos;

    int turn = 0;
    while(getline(ss,num,',')){
        curr = stoi(num);
        // log(curr);
        last_pos[prev] = turn;
        prev = curr;
        turn++;
    }

    for(;turn < TURNS; turn++){
        bool met = last_pos.find(curr) != last_pos.end();
        if(met){
            curr = turn - last_pos[curr];
        } else {
            curr = 0;
        }
        // log(curr);
        last_pos[prev] = turn;
        prev = curr;
    }
    return curr;
}

int main(int argc, char *argv[]) {
    // stringstream ss ("0,3,6");
    stringstream ss("14,3,1,0,9,5");

    cout << part1(ss) << '\n';
    return 0;
}
