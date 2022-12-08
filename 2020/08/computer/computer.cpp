#include <iostream>
#include <map>
#include "computer.h"
using namespace std;

std::map<std::string,int> opcodes {{"acc", 0}, {"jmp", 1}, {"nop", 2}};

Computer::Computer(){
    this->ac = 0;
    this->ip = 0;
}

int Computer::get_ac(){
    return this->ac;
}

void Computer::set_ac(int a){
    this->ac = a;
}

void Computer::run(instr instr){
    cout << "Executing: " << instr.opcode << ' ' << instr.arg0 << '\n';
    switch(instr.opcode){
        case 0:
            acc(instr.arg0); break;
        case 1:
            jmp(instr.arg0); break;
        case 2:
            nop(); break;
    }
}

void Computer::run(vector<instr> instrls){
    for(instr instr : instrls){
        cout << "Executing: " << instr.opcode << ' ' << instr.arg0 << '\n';
        run(instr);
    }
}

void Computer::acc(int i){
    this->ac += i;
    this->ip++;
}

void Computer::jmp(int i){
    this->ip += i;
}

void Computer::nop(){
    return;
}
