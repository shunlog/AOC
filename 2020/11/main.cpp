#include <iostream>
#include <vector>
#include <fstream>
#define FN "in.txt"
#define test test

using namespace std;

void printVec(vector<vector<int>> &v);
int solve1(vector<vector<int>> seats);
int solve2(vector<vector<int>> seats);


int main(int argc, char *argv[]) {
    ifstream f(FN);
    string line;
    vector<vector<int>> seats;

    int y = 0;
    while(getline(f,line)){
        seats.push_back(vector<int>());
        for(char ch : line){
            if(ch == 'L')
                seats[y].push_back(0);
            else
                seats[y].push_back(2);
        }
        y++;
    }



    cout << "Silver: " << solve1(seats) << '\n';
    cout << "Gold: " << solve2(seats) << '\n';

    return 0;
}

void printVec(vector<vector<int>> &v){
    for(uint y = 0; y < v.size(); y++){
        for(uint x = 0; x < v[y].size(); x++){
            if(v[y][x]==1){
                // cout << '#'; continue;
            }
            if(v[y][x]==2){
                // cout << '.'; continue;
            }
            if(v[y][x]==0){
                // cout << 'L'; continue;
            }
            // cout << v[y][x];
        }
        // cout << '\n';
    }
}

int solve1(vector<vector<int>> seats){

    bool changed = true;

    while(changed){
        vector<vector<int>> newVec;
        newVec = seats;
        changed = false;
        for(int sy = 0; sy < (int)seats.size(); sy++){
            for(int sx = 0; sx < (int)seats[0].size(); sx++){
                if(seats[sy][sx] == 2){
                    newVec[sy][sx] = 2;
                    continue;
                }

                int adj = 0;
                for(int y = -1; y <= 1; y++){
                    for(int x = -1; x <= 1; x++){
                        if((x == 0 && y == 0) ||
                           (sx+x < 0) || (sx+x >= (int)seats[0].size()) ||
                           (sy+y < 0) || (sy+y >= (int)seats.size()))
                            continue;
                        if(seats[sy+y][sx+x] == 1)
                            adj++;
                    }
                }
                if(seats[sy][sx] == 0 && adj == 0){
                    newVec[sy][sx] = 1;
                    changed = true;
                }
                else if(seats[sy][sx] == 1 && adj >= 4){
                    newVec[sy][sx] = 0;
                    changed = true;
                }
            }
        }

        seats = newVec;
        // cout << "----------------------------\n";
        // printVec(seats);
    }

    int count = 0;
    for(auto i:seats){
        for(auto j:i){
            if(j == 1) count++;
        }
    }
    return count;
}

int solve2(vector<vector<int>> seats){

    bool changed = true;
    while(changed){
        vector<vector<int>> newVec;
        newVec = seats;
        changed = false;
        for(int sy = 0; sy < (int)seats.size(); sy++){
            for(int sx = 0; sx < (int)seats[0].size(); sx++){
                if(seats[sy][sx] == 2){
                    newVec[sy][sx] = 2;
                    continue;
                }

                // count seen occupied seats
                int adj = 0, found;
                // down-right
                found = 2;
                for(int x=1, y=1; (sx+x < (int)seats[0].size()) &&
                    (sy+y < (int)seats.size()); x++, y++){
                    found = seats[sy+y][sx+x];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }
                // right
                found = 2;
                for(int x=1; sx+x < (int)seats[0].size(); x++){
                    found = seats[sy][sx+x];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }
                // top-right
                found = 2;
                for(int x=1, y=-1; (sx+x < (int)seats[0].size()) &&
                    (sy+y >= 0); x++, y--){
                    found = seats[sy+y][sx+x];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }
                // top
                found = 2;
                for(int y=-1; sy+y >= 0; y--){
                    found = seats[sy+y][sx];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }
                // top-left
                found = 2;
                for(int x=-1, y=-1; (sx+x >= 0) &&
                    (sy+y >= 0); x--, y--){
                    found = seats[sy+y][sx+x];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }
                // left
                found = 2;
                for(int x=-1; sx+x >= 0; x--){
                    found = seats[sy][sx+x];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }
                // down-left
                found = 2;
                for(int x=-1, y=1; (sx+x >= 0) &&
                    (sy+y < (int)seats.size()); x--, y++){
                    found = seats[sy+y][sx+x];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }
                // down
                found = 2;
                for(int y=1; sy+y < (int)seats.size(); y++){
                    found = seats[sy+y][sx];
                    if(found != 2){
                        if(found == 1) adj++;
                        break;
                    }
                }

                // rules
                if(seats[sy][sx] == 0 && adj == 0){
                    newVec[sy][sx] = 1;
                    changed = true;
                }
                else if(seats[sy][sx] == 1 && adj >= 5){
                    newVec[sy][sx] = 0;
                    changed = true;
                }
            }
        }

        seats = newVec;
        // cout << seats.size() << ' ' << seats[0].size() << '\n';
        // cout << "----------------------------\n";
        // printVec(seats);
    }

    int count = 0;
    for(auto i:seats){
        for(auto j:i){
            if(j == 1) count++;
        }
    }
    return count;
}
