#include <iostream>
#include <fstream>
#include <string>
#include <regex>

using namespace std;
string replace_all(string str, string from, int len, string to){
    int found = 0;
    while((found = str.find(from, found)) != string::npos){
      str.replace(found, len, to);
      found += to.size();
    }
    return str;
}

int main(int argc, char *argv[]) {

  ifstream f;
  if(argc != 2) exit(1);
  f.open(argv[1]);

  int total_literals = 0, total_memory = 0;
  string line;
  while(getline(f, line)){
    cout << "Analyzing: " << line << endl;
    cout << "Size: " << line.size() << endl;
    total_literals += line.size();

    string parsed = line.substr(1, line.size()-2);
    parsed = replace_all(parsed, "\\\\", 2, "\\");
    parsed = replace_all(parsed, "\\\"", 2, "\"");
    parsed = replace_all(parsed, "\\x", 4, "H");
    cout << "Parsed: " << parsed << endl;
    cout << "Size: " << parsed.size() << endl << endl;

    total_memory += parsed.size();
  }


    f.clear();
    f.seekg(0, f.beg);

  int total_new_literals = 0;
  total_literals = 0;

  while(getline(f, line)){
    cout << "Analyzing: " << line << endl;
    cout << "Size: " << line.size() << endl;
    total_literals += line.size();

    string parsed = line;
    parsed = replace_all(parsed, "\\\\", 2, "\\\\\\\\");
    parsed = replace_all(parsed, "\\\"", 2, "\\\\\\\"");
    parsed = replace_all(parsed, "\\x", 4, "\\\\xHH");
    parsed.replace(0, 1, "\\\"");
    parsed.replace(parsed.size()-1, 1, "\\\"");
    parsed = "\"" + parsed + "\"";

    cout << "Parsed: " << parsed << endl;
    cout << "Size: " << parsed.size() << endl << endl;

    total_new_literals += parsed.size();
  }

  cout << "Total: " << total_literals << endl;
  cout << "Less: " << total_memory << endl;
  cout << "More: " << total_new_literals << endl;

  cout << "Part 1: " << total_literals - total_memory << '\n';
  cout << "Part 2: " << total_new_literals - total_literals << '\n';
  return 0;
}
