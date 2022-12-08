#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <regex>
#define FN "in.txt"
using namespace std;

map<string,int> entries {{"byr",0}, {"iyr",1}, {"eyr",2}, {"hgt",3}, {"hcl",4}, {"ecl",5}, {"pid",6}, {"cid",7}};

bool is_valid(string entry, string value);
bool valid_byr(string value);
bool valid_iyr(string value);
bool valid_eyr(string value);
bool valid_hgt(string value);
bool valid_hcl(string value);
bool valid_ecl(string value);
bool valid_pid(string value);
bool valid_cid(string value);
bool valid_pass(vector<bool> &);

int main(int argc, char *argv[]){
    ifstream f(FN);
    int sol = 0;

    string s;
    vector<bool> pass(8);
    while(getline(f, s)){
        if(s == ""){
            if(valid_pass(pass))
                sol++;
            vector<bool> new_vec(8);
            pass = new_vec;
        } else {
            stringstream ss(s);
            string word;
            while(ss >> word){
                string entry = word.substr(0, word.find(":"));
                pass[entries[entry]] = true;
            }
        }
    }
    // last time
    if(valid_pass(pass))
        sol++;

    cout << "Silver: " << sol << '\n';

    f.close();
    f.open(FN);
    sol = 0;

    vector<bool> new_pass(8);
    pass = new_pass;
    while(getline(f, s)){
        if(s == ""){
            if(valid_pass(pass))
                sol++;
            vector<bool> new_vec(8);
            pass = new_vec;
        } else {
            stringstream ss(s);
            string word;
            while(ss >> word){
                string entry = word.substr(0, word.find(":"));
                string value = word.substr(word.find(":")+1);
                if(is_valid(entry, value)){
                    pass[entries[entry]] = true;
                }

            }
        }
    }
    // last time
    if(valid_pass(pass))
        sol++;

    cout << "Gold: " << sol << '\n';
    return 0;
}

bool valid_pass(vector<bool> &pass){
    bool valid = true;
    for(int i = 0; i < pass.size(); i++){
        if(i == entries["cid"]) continue;
        valid &= pass[i];
    }
    if (valid){
        return true;
    }
    return false;
}

bool is_valid(string entry, string value){
    switch(entries[entry]){
    case 0:
        return valid_byr(value);
    case 1:
        return valid_iyr(value);
    case 2:
        return valid_eyr(value);
    case 3:
        return valid_hgt(value);
    case 4:
        return valid_hcl(value);
    case 5:
        return valid_ecl(value);
    case 6:
        return valid_pid(value);
    case 7:
        return valid_cid(value);
    }
    cout << entry << ' ' << value; return false;
}
bool valid_byr(string value){
    try{
        int y = stoi(value);
        if(to_string(y).size() == value.size())
            return (y >= 1920) && (y <= 2002);
        return false;
    } catch(...) {
        return false;
    }
}
bool valid_iyr(string value){
    try{
        int y = stoi(value);
        if(to_string(y).size() == value.size())
            return (y >= 2010) && (y <= 2020);
        return false;
    } catch(...) {
        return false;
    }
}
bool valid_eyr(string value){
    try{
        int y = stoi(value);
        if(to_string(y).size() == value.size())
            return (y >= 2020) && (y <= 2030);
        return false;
    } catch(...) {
        return false;
    }
}
bool valid_hgt(string value){
    try{
        if (value.substr(value.size()-2) == "cm"){
            int s = stoi(value.substr(0,value.size()-2));
            if(to_string(s).size() == value.size()-2)
                return (s >= 150) && (s <= 193);
            return false;
        }
        if (value.substr(value.size()-2) == "in"){
            int s = stoi(value.substr(0,value.size()-2));
            if(to_string(s).size() == value.size()-2)
                return (s >= 59) && (s <= 76);
            return false;
        }
        return false;
    } catch(...) {
        return false;
    }
}
bool valid_hcl(string value){
    regex e ("#[0-9a-f]{6}");
    return regex_match(value, e);
}

bool valid_ecl(string value){
    regex e("(amb|blu|brn|gry|grn|hzl|oth)");
    return regex_match(value, e);
}

bool valid_pid(string value){
    regex e("[0-9]{9}");
    return regex_match(value, e);
}

bool valid_cid(string value){
    return true;
}

