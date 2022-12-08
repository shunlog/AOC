#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#define FN "in.txt"

using namespace std;

map<string,int> opcodes {{"acc", 0}, {"jmp", 1}, {"nop", 2}};

struct instruction{
    int opcode; // 0 - acc, 1 - jmp, 2 - nop
    int arg;
};

int main(int argc, char *argv[]) {
    vector<instruction> instl;

    ifstream f(FN);
    string line;
    while(getline(f, line)){
        stringstream ss(line);
        int opcode, arg;
        string sop, sarg;
        ss >> sop >> sarg;
        opcode = opcodes[sop];
        arg = stoi(sarg);
        cout << opcode << '\n';
        instl.push_back(instruction{opcode, arg});
    }

    int acc = 0;
    int pos = 0;
    bool visited[1000];

    while(true){
        instruction instr = instl[pos];
        if(visited[pos] == true){
            cout << "Silver: " << acc << '\n';
            break;
        }
        visited[pos] = true;
        switch(instr.opcode){
            case 0:
                acc += instr.arg;
                pos++;
                break;
            case 1:
                pos += instr.arg;
                break;
            case 2:
                pos++;
                break;
            default:
                cout << "Default?";
        }
    }
    return 0;
}
