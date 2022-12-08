#include <iostream>
#include <fstream>
#include <vector>
#define log(x) cout << #x << " = " << x << '\n';

using namespace std;
using bool_matrix = vector<vector<bool>>;

const int W = 100;
const int H = 100;
const string FN = "in.txt";
const int CYCLES = 100;

bool_matrix read_matrix(string fn, int W, int H);
bool_matrix step(bool_matrix area, bool part2);

int solve(string fn, bool part2 = false){
    bool_matrix area = read_matrix(FN, W, H);

    for(int i = 0; i < CYCLES; i++){
        area = step(area, part2);
    }
    if (part2)
        area[0][0] = area[H-1][W-1] = area[0][W-1] = area[H-1][0] = 1;
    int c = 0;
    for(int y = 0; y < H; y++){
        for(int x = 0; x < W; x++){
            if(area[y][x]) c++;
        }
    }
    return c;
}

int main(){
    cout << "Silver: " << solve(FN) << endl;
    cout << "Gold: " << solve(FN, true) << endl;
    return 0;
}
