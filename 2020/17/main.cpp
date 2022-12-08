#include <iostream>
#include <fstream>
#include <vector>
#include <map>

#define log(x) cout << #x << " = " << x << '\n';

#define FN "test.txt"
#define CYCLES 6

using namespace std;

using cube = bool;
using strip = map<int,cube>;
using area = map<int,strip>;
using space = map<int,area>;
using spacetime = map<int,space>;

class Spacetime{
private:
    int x0=0,x1=0,y0=0,y1=0,z0=0,z1=0,t0=0,t1=1;
    spacetime S;
public:
    struct range{
        int x0,x1,y0,y1,z0,z1,t0,t1;
    };

    void print(){
        cout << "==========\n";
        for(int t = t0; t <= t1; t++){
            if(t != t0) cout << "----------\n";
            for(int z = z0; z <= z1; z++){
                if(z != z0) cout << "..........\n";
                for(int y = y0; y <= y1; y++){
                    for(int x = x0; x <= x1; x++){
                        cout << S[t][z][y][x];
                    }
                    cout << '\n';
                }
            }
        }
    }
    void toggle(int t, int z, int y, int x, int n=-1){
        if(n == -1) S[t][z][y][x] = !S[t][z][y][x];
        else S[t][z][y][x] = n;
        if(x < x0) x0 = x; else if(x > x1) x1 = x;
        if(y < y0) y0 = y; else if(y > y1) y1 = y;
        if(z < z0) z0 = z; else if(z > z1) z1 = z;
        if(t < t0) t0 = t; else if(t > t1) t1 = t;
    }
    range get_range(){
        return range{x0,x1,y0,y1,z0,z1,t0,t1};
    }
    bool is_on(int t,int z, int y, int x){
        return S[t][z][y][x];
    }
    int count_on(){
        int c = 0;
        for(int t = t0; t <= t1; t++){
            for(int z = z0; z <= z1; z++){
                for(int y = y0; y <= y1; y++){
                    for(int x = x0; x <= x1; x++){
                        if(this->is_on(t,z,y,x)) c++;
                    }
                }
            }
        }
        return c;
    }
    int neighbors_on(int ti, int zi, int yi, int xi){
        int c = 0;
        for(int t = ti-1; t <= ti+1; t++){
            for(int z = zi-1; z <= zi+1; z++){
                for(int y = yi-1; y <= yi+1; y++){
                    for(int x = xi-1; x <= xi+1; x++){
                        if(!(z == zi && y == yi && x == xi && t == ti) && S[t][z][y][x])
                        c++;
                }
            }
        }
    }
    return c;
}
    };

int main(int argc, char *argv[]) {

    ifstream f(FN);
    string line;
    Spacetime S;

    int z = 0;
    int t = 0;
    int y = 0;
    while(getline(f,line)){
        int x = 0;
        for(char ch : line){
            if(ch == '#') S.toggle(t,z,y,x,1);
            x++;
        }
        y++;
    }


    for(int i = 0; i < CYCLES; i++){
        Spacetime S2(S);

        Spacetime::range r = S.get_range();
        for(int t = r.t0-1; t <= r.t1+1; t++){
            for(int z = r.z0-1; z <= r.z1+1; z++){
                for(int y = r.y0-1; y <= r.y1+1; y++){
                    for(int x = r.x0-1; x <= r.x1+1; x++){
                        if (S.is_on(t,z,y,x)){
                            if(!(S.neighbors_on(t,z,y,x) == 2 || S.neighbors_on(t,z,y,x) == 3))
                                S2.toggle(t,z,y,x,0);
                        } else {
                            if(S.neighbors_on(t,z,y,x) == 3)
                                S2.toggle(t,z,y,x,1);
                        }
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
