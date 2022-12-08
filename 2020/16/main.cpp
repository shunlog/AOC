#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#define FN "in.txt"

using namespace std;
using range = pair<int,int>;
using field = vector<range>;

vector<int> read_line(string line){
    vector<int> vec;
    string s;
    stringstream ss(line);
    while(getline(ss,s,',')){
        vec.push_back(stoi(s));
    }
    return vec;
}

bool is_contained(int n,field f){
    if((f[0].first <= n && n <= f[0].second)
       || (f[1].first <= n && n <= f[1].second)){

        return true;
    }
    return false;
}

int main(int argc, char *argv[]) {
    vector<field> fields;

    ifstream f(FN);
    string line;
    while (getline(f,line) && line != ""){
        while (line.find('-') != string::npos)
            line.replace(line.find('-'), 1, " ");
        stringstream ss(line);
        string junk;
        int st, fin;
        ss >> junk >> st >> fin;
        range r1(st,fin);
        ss >> junk >> st >> fin;
        range r2(st,fin);
        fields.push_back(field{r1,r2});
    }

    // skip this
    while (getline(f,line) && line != ""){};
    getline(f,line);

    // for(field f : fields){
    //     for(range r : f){
    //         cout << r.first << '-' << r.second << ", ";
    //     }
    //     cout << '\n';
    // }

    vector<set<int>> possible_fields(fields.size()); // contains a set of possible fields for each position
    for(int i = 0; i < fields.size(); i++){
        for(int j = 0; j < fields.size(); j++){
            possible_fields[i].insert(j);
        }
    }

    while (getline(f,line)){
        for(int f = 0; f < fields.size(); f++){
            // cout << "Checking field " << f << '\n';
            int pos = 0;
            for(int n : read_line(line)){
                if (!is_contained(n,fields[f])){
                    // cout << "Erasing possible field " << f << " from position " << pos << '\n';
                    possible_fields[pos].erase(f);
                }
            pos++;
            }
        }
    }

    for(set<int> set : possible_fields){
        for(int i : set){
            cout << i << ' ';
        }
        cout << '\n';
    }
    // cout << "Silver: " << sum << '\n';
    return 0;
}
