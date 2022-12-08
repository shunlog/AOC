#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(){
  ifstream file("data.txt");
  int sum = 0;
  int module_fuel = 0;

  while(file){
    int mass = 0;

    file >> mass;
    if (mass != 0){
      module_fuel += int(floor(mass/3)-2);
      int prev_fuel = mass;
      int total_fuel = 0;

      
      while(1){
        int bonus_fuel;
        bonus_fuel = int(floor(prev_fuel/3)-2); 
        if (bonus_fuel>0){
          total_fuel += bonus_fuel;
          prev_fuel = bonus_fuel;
        } else break;
      } 

      sum += total_fuel;
    }
  }

  cout << "First part: " << module_fuel << endl;
  cout << "Second part: " << sum << endl;
  
  return 0;
}
