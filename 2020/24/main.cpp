#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#define FN "in.txt"
#define STEPS 100
#define log(x) cout << #x << " = " << x << '\n';

using namespace std;
using tile = pair<int,int>;

// after toggling a tile to black, insert the white tiles around it into the map too
void check_around(tile t, map<tile,bool> &floor){
    for(int j = -1; j <= 1; j++){
        for(int k = -1; k <= 1; k++){
            tile t2{t.first + j, t.second + k};
            if(j != k && floor.find(t2) == floor.end())
                floor[t2] = false;
        }
    }
}

int count_neighbors(tile t, const map<tile,bool> &floor){
    int c = 0;
    for(int j = -1; j <= 1; j++){
        for(int k = -1; k <= 1; k++){
            tile t2{t.first + j, t.second + k};
            if(j != k && floor.find(t2) != floor.end() && floor.at(t2))
                c++;
        }
    }
    return c;
}

bool check_tile(tile t, map<tile,bool> &floor){
    if(floor.find(t) != floor.end() && floor.at(t)){ // black t
        int neighbors = count_neighbors(t, floor);
        if(neighbors == 0 || neighbors > 2){
            return false;
        }
    } else { // white t
        int neighbors = count_neighbors(t, floor);
        if(neighbors == 2){
            return true;
        }
    }
    return floor.at(t);
}

int main(int argc, char *argv[]) {
    ifstream f(FN);
    string line;

    map<tile,bool> floor;

    while(getline(f,line)){
        stringstream ss(line);
        char ch;
        int j = 0, k = 0;

        while(ss >> ch){
            switch(ch){
            case 'e': j++; k--; break;
            case 'w': j--; k++; break;
            case 's':
                ss >> ch;
                switch(ch){
                case 'e': k--; break;
                case 'w': j--; break;
                } break;
            case 'n':
                ss >> ch;
                switch(ch){
                case 'e': j++; break;
                case 'w': k++; break;
                } break;
            }
        }
        floor[tile(j,k)] = !floor[tile(j,k)];
        if(floor[tile(j,k)]){ // turned tile to black
            check_around(tile(j,k), floor);
        }
    }

    int sum = 0;
    for(auto i : floor){
        if(i.second) sum++;
    }
    cout << "Silver: " << sum << '\n';

    for(int s = 0; s < STEPS; s++){
        map<tile,bool> floor_cpy = floor;
        // check the tiles in the map
        for(pair<tile,bool> p : floor){
            floor_cpy[p.first] = check_tile(p.first, floor);
            if(floor_cpy[p.first]) // turned to black
                check_around(p.first, floor_cpy);
        }
        // also have to check for white adjacent tiles that are not in the map
        floor = floor_cpy;
    }

    sum = 0;
    for(auto i : floor){
        if(i.second) sum++;
    }
    cout << "Gold: " << sum << '\n';

    return 0;
}
