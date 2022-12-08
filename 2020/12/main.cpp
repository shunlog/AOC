#include <iostream>
#include <fstream>
#include <tuple>
#define FN "in.txt"

using namespace std;

pair<int,int> rotate(int x0, int y0, int deg){
    int x,y;
    switch(deg){
        case 0: x=0; y=0; break;
        case 90: x=y0; y=-x0; break;
        case 180: x=-x0; y=-y0; break;
        case 270: x=-y0; y=x0; break;
    }
    return pair<int,int>(x,y);
}

int main(int argc, char *argv[]) {
    int deg = 0; //east
    int x = 0, y = 0;

    ifstream f(FN);
    string line;
    while(getline(f, line)){
        int arg = stoi(line.substr(1));
        switch(line[0]){
            case 'F':
                switch(deg){
                    case 0: x += arg; break;
                    case 90: y -= arg; break;
                    case 180: x -= arg; break;
                    case 270: y += arg; break;
                    default: cout << "W1\n"; return 1;
                }
                break;
            case 'R': deg = (deg + arg) % 360; break;
            case 'L': deg = (deg - arg + 360) % 360; break;
            case 'N': y += arg; break;
            case 'S': y -= arg; break;
            case 'E': x += arg; break;
            case 'W': x -= arg; break;
        }
    }

    cout << "Silver: " << abs(x)+abs(y) << '\n';

    f.close();
    f.open(FN);
    x = 0; y = 0;
    int wx = 10, wy = 1; // waypoint coords
    while(getline(f, line)){
        int arg = stoi(line.substr(1));
        pair<int,int> p;
        switch(line[0]){
            case 'F':
                x += arg * wx;
                y += arg * wy;
                break;
            case 'R': tie(wx,wy) = rotate(wx,wy,arg); break;
            case 'L': tie(wx,wy) = rotate(wx,wy,(360-arg)%360); break;
            case 'N': wy += arg; break;
            case 'S': wy -= arg; break;
            case 'E': wx += arg; break;
            case 'W': wx -= arg; break;
            default:
                cout << line << '\n'; return 1;
        }
    }
    cout << "Gold: " << abs(x) + abs(y) << '\n';

    return 0;
}
