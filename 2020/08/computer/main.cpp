#include <iostream>
#include <fstream>
#include <vector>
#include "computer.h"

using namespace std;

int main(int argc, char *argv[]) {

    Computer comp;
    ifstream f("in.txt");

    string line;
    while(getline(f,line)){
        int opcode = opcodes[line.substr(0,line.find(' '))];
        int arg0 = stoi(line.substr(line.find(' ')));
        instr ins {opcode,arg0};
        comp.run(ins);
        cout << comp.get_ac() << '\n';
    }

    return 0;
}
