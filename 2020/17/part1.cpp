#include <iostream>
#include <fstream>
#include <vector>
#include <map>

#define log(x) cout << #x << " = " << x << '\n';

#define FN "in.txt"
#define CYCLES 6

using namespace std;

using cube = bool;
using strip = map<int,cube>;
using area = map<int,strip>;
using space = map<int,area>;

class Space{
private:
    int x0=0,x1=0,y0=0,y1=0,z0=0,z1=0;
    space S;
public:
    struct range{
        int x0,x1,y0,y1,z0,z1;
    };

    void print(){
        cout << "==========\n";
        for(int z = z0; z <= z1; z++){
            if(z != z0) cout << "----------\n";
            for(int y = y0; y <= y1; y++){
                for(int x = x0; x <= x1; x++){
                    cout << S[z][y][x];
                }
                cout << '\n';
            }
        }
    }
    void toggle(int z, int y, int x, int n=-1){
        if(n == -1) S[z][y][x] = !S[z][y][x];
        else S[z][y][x] = n;
        if(x < x0) x0 = x; else if(x > x1) x1 = x;
        if(y < y0) y0 = y; else if(y > y1) y1 = y;
        if(z < z0) z0 = z; else if(z > z1) z1 = z;
    }
    range get_range(){
        return range{x0,x1,y0,y1,z0,z1};
    }
    bool is_on(int z, int y, int x){
        return S[z][y][x];
    }
    int count_on(){
        int c = 0;
        for(int z = z0; z <= z1; z++){
            for(int y = y0; y <= y1; y++){
                for(int x = x0; x <= x1; x++){
                    if(this->is_on(z,y,x)) c++;
                }
            }
        }
        return c;
    }
    int neighbors_on(int zi, int yi, int xi){
        int c = 0;
        for(int z = zi-1; z <= zi+1; z++){
            for(int y = yi-1; y <= yi+1; y++){
                for(int x = xi-1; x <= xi+1; x++){
                    if(!(z == zi && y == yi && x == xi) && S[z][y][x])
                        c++;
                }
            }
        }
        return c;
    }
};

int main(int argc, char *argv[]) {

    ifstream f(FN);
    string line;
    Space S;

    int z = 0;
    int y = 0;
    while(getline(f,line)){
        int x = 0;
        for(char ch : line){
            if(ch == '#') S.toggle(z,y,x,1);
            x++;
        }
        y++;
    }


    for(int i = 0; i < CYCLES; i++){
        Space S2(S);

        Space::range r = S.get_range();
        for(int z = r.z0-1; z <= r.z1+1; z++){
            for(int y = r.y0-1; y <= r.y1+1; y++){
                for(int x = r.x0-1; x <= r.x1+1; x++){
                    if (S.is_on(z,y,x)){
                        if(!(S.neighbors_on(z,y,x) == 2 || S.neighbors_on(z,y,x) == 3))
                            S2.toggle(z,y,x,0);
                    } else {
                        if(S.neighbors_on(z,y,x) == 3)
                            S2.toggle(z,y,x,1);
                    }
                }
            }
        }

        S = S2;
        // S.print();
    }

    cout << "Silver: " << S.count_on();
    return 0;
}
