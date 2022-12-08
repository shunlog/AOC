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
        instl.push_back(instruction{opcode, arg});
    }


    for(uint i=0; i < instl.size(); i++){

        if(instl[i].opcode == 1)
            instl[i].opcode = 2;
        else if(instl[i].opcode == 2)
            instl[i].opcode = 1;

        int acc = 0;
        uint pos = 0;
        vector<bool> visited;
        visited.resize(1000);

        bool stalled = false;
        while(true){
            if(pos >= instl.size()){
                cout << "Gold: " << acc << '\n';
                break;
            }
            instruction instr = instl[pos];
            if(visited[pos]){
                stalled = true;
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
        if (!stalled)
            break;

        // reverse the change
        if(instl[i].opcode == 1)
            instl[i].opcode = 2;
        else if(instl[i].opcode == 2)
            instl[i].opcode = 1;
    }
    return 0;
}
