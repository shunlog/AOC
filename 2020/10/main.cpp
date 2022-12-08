#include <iostream>
#include <set>
#include <fstream>
#include <map>
#define FN "test2.txt"

using namespace std;
int solve1(set<int> &s);
long long solve2(set<int> &s);
long long branches(int i, const set<int> &rates, map<int,long long> &known);

int main(int argc, char *argv[]) {

    set<int> rates;

    ifstream f(FN);
    string line;
    while(getline(f,line)){
        rates.insert(stoi(line));
    }
    rates.insert(0);
    rates.insert(*rates.rbegin()+3);

    cout << "Silver: " << solve1(rates) << '\n';
    cout << "Gold: " << solve2(rates) << '\n';
    return 0;
}

int solve1(set<int> &rates){
    int diff1 = 0, diff3 = 0;
    int prev = 0;
    for(auto j : rates){
        if(j - prev == 1)
            diff1++;
        else if(j - prev == 3)
            diff3++;
        prev = j;
    }
    diff3++; // device adapter
    return diff1 * diff3;
}

long long solve2(set<int> &rates){

    map<int,long long> known;
    return branches(*rates.rbegin(), rates, known);
}

long long branches(int i, const set<int> &rates, map<int,long long> &known){
    if(rates.find(i) == rates.begin()){
        return 1;
    }

    if(known[i]){
        return known[i];
    }

    long long n = 0;
    for(int j = 1; j < 4; j++){
        if(rates.find(i-j) != rates.end()){
            n += branches(i-j, rates, known);
        }
    }
    known[i] = n;

    return n;
}
