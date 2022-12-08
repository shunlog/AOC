#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

struct wire_pos {
    int x;
    int y;
    int len;
};

struct dir_steps{
    int dir[2]; // x and y to sum to the previous pos e.g. [1, 0] for R
    int steps;
};

enum directions{ R, D, L, U};

vector<dir_steps> read_data(string line);
dir_steps create_dir_steps(char dir, int steps);
// returns 0 if no intersection, else len of the wire pos from wl
int intersects(wire_pos wp, vector<wire_pos> wl);

int main(int argc, char *argv[]) {

    if(argc != 2) {
        puts("Give filename!");
        return 1;
    }

    string fn = argv[1];
    ifstream f;
    f.open(fn);

    string line;
    getline(f, line);
    vector<dir_steps> ds_ls = read_data(line);

    getline(f, line);
    vector<dir_steps> ds_ls2 = read_data(line);

    // create list of all wire1 positions
    vector<wire_pos> w1;
    int x = 0;
    int y = 0;
    int len = 0;
    for(dir_steps ds : ds_ls){
        for (int i = 0; i < ds.steps; i++) {
            x += ds.dir[0];
            y += ds.dir[1];
            len += 1;
            wire_pos current_pos = {x, y, len};
            w1.push_back(current_pos);
        }
    }
    // get intersections and compute the solution
    x = y = len = 0;
    uint min_mhtn_dist = -1;
    uint min_len = -1;

    for(dir_steps ds : ds_ls2){
        for (int i = 0; i < ds.steps; i++) {
            x += ds.dir[0];
            y += ds.dir[1];
            len += 1;
            wire_pos current_pos = {x, y, len};

            int wp1_len = intersects(current_pos, w1); // returns false if no intersection
            if(wp1_len){
                // cout << "Intersection: "
                //     << current_pos.x << ' ' << current_pos.y << ' '
                //      << wp1_len << ' ' << current_pos.len << endl;

                uint mhtn_dist = abs(x) + abs(y);
                uint len_sum = current_pos.len + wp1_len;
                min_mhtn_dist = min(min_mhtn_dist, mhtn_dist);
                min_len = min(len_sum, min_len);
            }
        }
    }
    cout << "Min dist: " << min_mhtn_dist << endl;
    cout << "Min len sum: " << min_len << endl;
    return 0;
}

// return a [List-of dir_steps]
vector<dir_steps> read_data(string line){
    vector<dir_steps> vec;

    stringstream ss(line);
    char dir, comma;
    int steps;

    while(ss >> dir >> steps >> comma){
        dir_steps ds = create_dir_steps(dir, steps);
        vec.push_back(ds);
    }
    ss >> dir >> steps;
    dir_steps ds = create_dir_steps(dir, steps);
    vec.push_back(ds);

    return vec;
}

dir_steps create_dir_steps(char dir, int steps){
    dir_steps ds;
    int x, y;
    switch (dir) {
    case 'R':
        x = 1;
        y = 0;
        break;
    case 'D':
        x = 0;
        y = 1;
        break;
    case 'L':
        x = -1;
        y = 0;
        break;
    case 'U':
        x = 0;
        y = -1;
        break;
    }

    ds.dir[0] = x;
    ds.dir[1] = y;
    ds.steps = steps;
    return ds;
}

int intersects(wire_pos wp2, vector<wire_pos> w1){
    for(wire_pos wp1: w1){
        if (wp2.x == wp1.x && wp2.y == wp1.y)
            return wp1.len;
    }
    return 0;
}
