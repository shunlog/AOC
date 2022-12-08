#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

struct instr_line{
  string op;
  string reg;
};
struct Reg{
  string name;
  uint16_t val;
};

// 1. create a vector of pair<string, string> Operations
// 2. make a function that takes a register as an input and recursively calculate's it's value
// 2.1. see if this register hasn't been calculated in a vector of pair<string, int>
// 2.2. if not, find it in Operations
// 2.3. calculate it if possible, doing the operation on the known registers/register
// 2.4. if not, recursively get the value of the unknown registers
// 2.5 calculate this register's value

static vector<instr_line> instr_lines;
static vector<Reg> registers;

uint16_t calc_reg(string reg);
string get_op(string reg_name);
bool contains(vector<string> v, string tok);
vector<string> split(const string &str, string delim);
bool is_numeric(string str);

int main(int argc, char *argv[]) {
  ifstream f;
  if(argc != 2) return 1;
  f.open(argv[1]);

  string line;
  while(getline(f, line)){
    int instr_pos = line.find(" -> ");
    string operation, reg;
    operation =  line.substr(0, instr_pos);
    reg = line.substr(instr_pos+4);
    instr_line ol = {operation, reg};
    instr_lines.push_back(ol);
  }

  cout << calc_reg("a");

  return 0;
}

uint16_t calc_reg(string reg_name){
  uint16_t reg_val;
  // check if this is just a number
  if(is_numeric(reg_name)){
    return stoi(reg_name);
  }

  // check if value of reg has been calculated
  for(Reg reg : registers){
    if(reg.name == reg_name)
      return reg.val;
  }

  string op = get_op(reg_name);
  cout << op << endl;
  vector<string> tokens = split(op, " ");
  if(contains(tokens, "AND")){
    reg_val = calc_reg(tokens[0]) & calc_reg(tokens[2]);
  }
  else if(contains(tokens, "OR")){
    reg_val = calc_reg(tokens[0]) | calc_reg(tokens[2]);
  }
  else if(contains(tokens, "NOT")){
    reg_val = ~calc_reg(tokens[1]);
  }
  else if(contains(tokens, "LSHIFT")){
    reg_val = calc_reg(tokens[0]) << stoi(tokens[2]);
  }
  else if(contains(tokens, "RSHIFT")){
    reg_val = calc_reg(tokens[0]) >> stoi(tokens[2]);
  }
  // just a reg name
  else{
    reg_val = calc_reg(tokens[0]);
  }

  // push this back to known registers
  Reg new_reg = {reg_name, reg_val};
  registers.push_back(new_reg);
  return reg_val;
}

string get_op(string reg_name){
  for(instr_line l : instr_lines){
    if (l.reg == reg_name){
      return l.op;
    }
  }
  cout << "Reg name:" << reg_name << "->";
  cout << "Can't find operation";
  exit(1);
}

vector<string> split(const string &str, string delim) {
  vector<string> tokens;
  string::size_type start = 0;
  string::size_type end = 0;

  while ((end = str.find(delim, start)) != string::npos) {
    tokens.push_back(str.substr(start, end - start));
    start = end + delim.size();
  }
  tokens.push_back(str.substr(start));
  return tokens;
}

bool contains(vector<string> v, string tok){
  for(auto i:v){
    if(i == tok) return true;
  }
  return false;
}

bool is_numeric(string str) {
  for (int i = 0; i < str.length(); i++)
    if (isdigit(str[i]) == false)
      return false; //when one non numeric value is found, return false
  return true;
}
