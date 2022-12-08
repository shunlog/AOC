#ifndef __COMPUTER_H_
#define __COMPUTER_H_

#include <vector>
#include <map>
#include <string>

extern std::map<std::string,int> opcodes;

struct instr{
    int opcode;
    int arg0;
};

class Computer{
private:
    int ac;
    int ip;
    void acc(int);
    void jmp(int);
    void nop();
public:
    Computer();
    int get_ac();
    void set_ac(int a);
    void run(instr);
    void run(std::vector<instr>);
};


#endif // __COMPUTER_H_
