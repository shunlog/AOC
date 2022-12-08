#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

//read the instr list from file
void parseIntcodeFile(vector <int> &instr){
    ifstream file;
    file.open("data.txt");

    string data;
    getline(file, data);

    stringstream ss(data);
    while(1){
        int num;
        char ch;
        ss >> num >> ch;
        instr.push_back(num);
        if(!ss) break;
    }

}

void printIntcode(vector <int> &instr){
    for(int i=0; i<int(instr.size()); i++){
        cout << instr[i] << ' ';
    }
}

void executeIntcode(vector <int> &instr){
    int p = 0;          // the pointer to a location in list
    bool halt = false;  // if instruction is 99 -> halt program

    while(1){
        int opcode = instr[p];
        switch(opcode){
            case 1: 
                instr[instr[p+3]] = instr[instr[p+1]]+instr[instr[p+2]];
                break;
            case 2: 
                instr[instr[p+3]] = instr[instr[p+1]]*instr[instr[p+2]];
                break;
            case 99:
                halt = true; 
                break;
        }
        if (halt) break;
        p += 4;
    }
}

int main(){
    // vector containing a list of instructions
    vector <int> instr;

    parseIntcodeFile(instr);


    // part 2 requires to find the input to get a specific output
    for(int i=0; i<100; i++){
        for(int j=0; j<100; j++){

            vector <int> instr_copy = instr;
            instr_copy[1] = i;
            instr_copy[2] = j;

            executeIntcode(instr_copy);
            int result = instr_copy[0];
            if (result == 19690720){
                cout << "Found expected inputs: " << i << " and " << j << endl;
                cout << "The solution is: " << i*100 + j;
                break;
            }
        }
    }


    return 0;
}
