#include <fstream>
#include <vector>

using namespace std;
using bool_matrix = vector<vector<bool>>;

bool_matrix gen_matrix(int W, int H){
    return bool_matrix(H, vector<bool> (W, 0));
}

bool_matrix step(bool_matrix area, bool part2){
    int H = area.size();
    int W = area[0].size();
    bool_matrix area_cpy = gen_matrix(W, H);
    if (part2)
        area[0][0] = area[H-1][W-1] = area[0][W-1] = area[H-1][0] = 1;
    for(int y = 0; y < H; y++){
        for(int x = 0; x < W; x++){
            //count neighbors
            int c = 0;
            for(int y0 = y-1; y0 <= y+1; y0++){
                for(int x0 = x-1; x0 <= x+1; x0++){
                    if((y0 == y && x0 == x) || y0 < 0 ||
                       x0 < 0 || y0 >= H || x0 >= W) continue;
                    if(area[y0][x0]) c++;
                }
            }
            if(area[y][x]){
                if(c == 2 || c==3) area_cpy[y][x] = true;
            } else {
                if (c == 3) area_cpy[y][x] = true;
            }
        }
    }
    area = area_cpy;
    return area;
}

bool_matrix read_matrix(string fn, int W, int H){
    bool_matrix area = gen_matrix(W, H);
    ifstream f(fn);
    string line;
    int y = 0;
    while(getline(f,line)){
        int x = 0;
        for(char ch: line){
            if(ch == '#') area[y][x] = true;
            x++;
        }
        y++;
    }
    return area;
}
