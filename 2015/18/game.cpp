#include "matrix.h"
#include <curses.h>
#include <chrono>
#include <thread>
#include <vector>
#include <string>

using namespace std;
using bool_matrix = vector<vector<bool>>;

const int W = 100;
const int H = 100;
const string FN = "in.txt";
const int CYCLES = 100;

int main(void)
{
    initscr();
    cbreak();
    noecho();
    clear();

    bool_matrix area = read_matrix(FN, W, H);

    for(int i = 0; i < CYCLES; i++){
        area = step(area);
        for(int y = 0; y < H; y++){
            for(int x = 0; x < W; x++){
                char* ch = area[y][x] ? (char *)"#" : (char *)".";
                mvaddstr(x, y, ch);
            }
        }
        refresh();
        std::this_thread::sleep_for(std::chrono::milliseconds(50) );
    }

    getch();
    endwin();
    return 0;
}
