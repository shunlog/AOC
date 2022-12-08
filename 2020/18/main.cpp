#include <iostream>
#include <fstream>
#include <stack>
#include <sstream>
#define FN "in.txt"
#define log(x) cout << #x << " = " << x << '\n';

using namespace std;
using ll = long long;

ll eval(string s){
    // log(s);

    // get rid of the parantheses first
    while(s.find('(') != string::npos){
        stack<char> br;
        int begin = s.find('(')+1, end = begin;
        br.push('(');

        for(char ch : s.substr(begin)){
            if(ch == ')')
                br.pop();
            else if(ch == '(')
                br.push('(');
            if(br.size() == 0) break;
            end++;
        }
        string sub = s.substr(begin,end-begin);
        s.replace(begin-1,end-begin+2,to_string(eval(sub)));
    }

    // put parantheses around the arguments of * so that it's done the last
    if(s.find('*') != string::npos){
        string s1 = s.substr(0,s.find('*')-1);
        string s2 = s.substr(s.find('*')+2);
        return eval(s1) * eval(s2);
    }

    // calculate the simplified expression
    ll r = 0;
    string token;
    string op = "+";
    ll n = 0;
    stringstream ss(s);
    while(getline(ss,token,' ')){
        if(token != "+" && token != "*"){
            switch(op[0]){
                case '+': r += stoll(token); break;
                case '*': r *= stoll(token); break; // it doesn't get here
            }
        } else {
            op = token;
        }
    }

    return r;
}

int main(int argc, char *argv[]) {
    ifstream f(FN);
    string line;
    ll S = 0;
    while(getline(f,line)){
        ll r = eval(line);
        // log(r);
        S += r;
    }

    cout << "Silver: " << S << '\n';


    return 0;
}
