#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#define FN "in.txt"

using namespace std;

vector<int> read_line(string line){
    vector<int> vec;
    string s;
    stringstream ss(line);
    while(getline(ss,s,',')){
        vec.push_back(stoi(s));
    }
    return vec;
}

int main(int argc, char *argv[]) {

    vector<pair<int,int>> ranges;

    ifstream f(FN);
    string line;
    while (getline(f,line) && line != ""){
        while (line.find('-') != string::npos)
            line.replace(line.find('-'), 1, " ");
        stringstream ss(line);
        string junk;
        for(int i = 0; i < 2; i++){
            int st, fin;
            ss >> junk >> st >> fin;
            ranges.push_back(pair<int,int> (st,fin));
        }
        // cout << line << '\n';
    }

    // skip this
    while (getline(f,line) && line != ""){};
    getline(f,line);

    int sum = 0;

    while (getline(f,line)){
        for(int n : read_line(line)){
            bool valid = false;
            for(auto range : ranges){
                if(range.first <= n && n <= range.second){
                    valid = true;
                    break;
                }
            }
            if (!valid){
                sum += n;
                // cout << n << " is valid\n";
            } else {
                // cout << n << " is invalid\n";
            }

        }
    }
    cout << "Silver: " << sum << '\n';
    return 0;
}
