#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;

map<string, int> Things{{"children",0}, {"cats",1}, {"samoyeds",2}, {"pomeranians",3}, {"akitas",4}, {"vizslas",5}, {"goldfish",6}, {"trees",7}, {"cars",8}, {"perfumes",9}};

int main(int argc, char *argv[]) {

    int things[] = {3, 7, 2, 3, 0, 0, 5, 3, 2, 1};
    {
    ifstream f("in.txt");
    string s;
    int aunt = 1;
    while(getline(f,s)){
        bool coincides = true;
        string temp, name;
        int n;
        stringstream ss(s);
        ss >> temp >> temp;
        while(ss >> name){
            name.pop_back();
            ss >> temp;
            n = stoi(temp);
            if (things[Things[name]] != n) {
                coincides = false;
                break;
            }
        }
        if(coincides){
            cout << "Silver: " << aunt << '\n';
            break;
        }
        aunt++;
    }
    }


    {
    ifstream f("in.txt");
    string s;
    int aunt = 1;
    while(getline(f,s)){
        bool coincides = true;
        string temp, name;
        int n;
        stringstream ss(s);
        ss >> temp >> temp;
        while(ss >> name){
            name.pop_back();
            ss >> temp;
            n = stoi(temp);
            int i = Things[name];
            if((i == 1 || i == 7 && things[i] >= n)
               || (i == 3 || i == 6 && things[i] <= n)
               || (i != 1 && i!=7 && i!= 3 && i!= 6 && things[i] != n)) {
                coincides = false;
                break;
            }
        }
        if(coincides){
            cout << "Gold: " << aunt << '\n';
            break;
        }
        aunt++;
    }
    }
    return 0;
}
