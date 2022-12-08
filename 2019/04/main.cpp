#include <iostream>
#include <sstream>
using namespace std;

bool has_double(int n){
  stringstream ss;
  char prev, current;
  ss << n;
  ss >> prev;
  while(ss >> current){
    if(prev == current)
      return true;
    prev = current;
  }
  return false;
}

// return true if there is at least one double that's not part of a triple
bool has_exact_double(int n){
  stringstream ss;
  char prev, current;
  int chain = 1;

  ss << n;
  ss >> prev;
  while(ss >> current){
    if (prev == current){
      chain++;
    } else if (prev != current && chain == 2){
      return true;
    } else {
      chain = 1;
    }
    prev = current;
  }

  if(chain == 2)
    return true;
  return false;
}

int main(int argc, char *argv[]) {
  int from = 372037;
  int to = 905157;

  int c1 = 0;
  int c2 = 0;

  for(int f = 3; f <= 9; f++){
    for(int e = f; e <= 9; e++){
      for(int d = e; d <= 9; d++){
        for(int c = d; c <= 9; c++){
          for(int b = c; b <= 9; b++){
            for(int a = b; a <= 9; a++){
              stringstream ss;
              ss << f << e << d << c << b << a;
              int n;
              ss >> n;
              if (from < n && n < to){
                cout << n;
                if (has_double(n)){
                  c1++;
                  if(has_exact_double(n)){
                    c2++;
                    cout << " passes!";
                  }
                }
                cout << '\n';
              }
            }}}}}}

  cout << "Count1: " << c1 << endl;
  cout << "Count2: " << c2 << endl;

  return 0;
}
