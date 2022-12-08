#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;


int main ()
{
  vector<vector<int>> data;
  string str;
  ifstream file("data10.txt");
  while (getline (file, str)){
    vector<int> arr;
    char buffer[6]; 
    int number;

    size_t length = str.copy(buffer, 6, 10);
    buffer[length]='\0';
    number = stoi(buffer);
    arr.push_back(number);

    length = str.copy(buffer, 6, 18);
    buffer[length]='\0';
    number = stoi(buffer);
    arr.push_back(number);
    
    length = str.copy(buffer, 2, 36);
    buffer[length]='\0';
    number = stoi(buffer);
    arr.push_back(number);

    length = str.copy(buffer, 2, 40);
    buffer[length]='\0';
    number = stoi(buffer);
    arr.push_back(number);

    data.push_back(arr);
  }

  int width, height, min_width = 10000000, min_height = 1000000; 
  int min_x, max_x, min_y, max_y, seconds_passed = 0;

  while(true){
    min_x = data[0][0];
    max_x = data[0][0];
    min_y = data[0][1];
    max_y = data[0][1];

    for(int i=0; i<int(data.size()); i++){
      data[i][0] += data[i][2];
      data[i][1] += data[i][3];
      if (data[i][0] > max_x){
        max_x = data[i][0];
      }
      if (data[i][0] < min_x){
        min_x = data[i][0];
      }
      if (data[i][1] > max_y){
        max_y = data[i][1];
      }
      if (data[i][1] < min_y){
        min_y = data[i][1];
      }
    }
    width = max_x - min_x;
    height = max_y - min_y;
    if(width < min_width){
      min_width = width;
      min_height = height;
      seconds_passed += 1;
    } else {
      cout << "\nmin_x = " << min_x;
      cout << "\nmax_x = " << max_x << "\n";
      cout << "\nmin_y = " << min_y;
      cout << "\nmax_y = " << max_y << "\n";
      break;
    }
  }

  //go back one step
  for(int i=0; i<int(data.size()); i++){
    data[i][0] -= data[i][2];
    data[i][1] -= data[i][3];
  }
  
  //create matrix
  vector<vector<char>> matrix;
  for(int i=0; i<min_height + 100; i++){
    matrix.push_back({});
    for(int j=0; j<min_width + 100; j++){
      matrix[i].push_back('.');
    }
  }

  //put the stars
  int x,y;
  for(int i=0; i<int(data.size()); i++){
    x = data[i][0] - min_x;
    y = data[i][1] - min_y;
    matrix[x][y] = '#';
  }

  //represent matrix
  ofstream o_file("output10.txt");
  for(int j=0; j<min_height + 20; j++){
    for(int i=0; i<min_width + 20; i++){
      o_file << matrix[i][j] << ' ';
    }
    o_file << endl;
  }
  
  cout << "\nPart two: seconds_passed = " << seconds_passed;

  return 0;
}

