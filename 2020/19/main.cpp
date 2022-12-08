#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <stack>
#include <sstream>
#define log(x) cout << #x << " = " << x << '\n';
#define FN "test.txt"

using namespace std;

using ll = long long;
map<int,string> rules;

string matches(string s, int rule, map<int,string> &rules){
    if (rules[rule][0] == '"'){
        char literal = rules[rule][1];
        if (s[0] == literal) return s.substr(1);
        return "E";
    }

    stack<int> rules_stack;


    return "";
}

int main(int argc, char *argv[]) {

    ifstream f(FN);
    string line;
    while(getline(f,line)){
        if(line == "") break;

        int col = line.find(':');
        int rn = stoi(line.substr(0,col));
        string s = line.substr(col+2);
        rules[rn] = s;
    }

    for(auto i : rules){
        cout << i.second << '\n';
    }

    return 0;
}
