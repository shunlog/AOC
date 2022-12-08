#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#define FN "in.txt"

using namespace std;

int main(int argc, char *argv[]) {

    {
        ifstream f(FN);
        string s;
        vector<vector<bool>> M;
        M.reserve(323);
        while(getline(f,s)){
            vector<bool> line;
            line.reserve(30);
            for(char ch : s){
                if(ch == '.')
                    line.push_back(false);
                else
                    line.push_back(true);
            }
            M.push_back(line);
        }

        int hits;
        int j = 0;
        for(int i = 0; i < M.size(); i++){
            if(M[i][j]) hits++;
            j = (j+3) % M[0].size();
        }

        cout << "Silver: " << hits << '\n';
    }

    {
        ifstream f(FN);
        string s;
        vector<vector<bool>> M;
        M.reserve(323);
        while(getline(f,s)){
            vector<bool> line;
            line.reserve(30);
            for(char ch : s){
                if(ch == '.')
                    line.push_back(false);
                else
                    line.push_back(true);
            }
            M.push_back(line);
        }

        long res = 1;
        vector<int> steps{1, 3, 5, 7};
        for(int step : steps){
            int hits = 0;
            int j = 0;
            for(int i = 0; i < M.size(); i++){
                if(M[i][j]) hits++;
                j = (j+step) % M[0].size();
            }
        cout << hits << '\n';
            res *= hits;
        }
        int hits = 0;
        int j = 0;
        for(int i = 0; i < M.size(); i+=2){
            if(M[i][j]) hits++;
            j = (j+1) % M[0].size();
        }
        cout << hits << '\n';
        res *= hits;

        cout << "Gold: " << fixed << std::setprecision(0)<< res << '\n';
    }
    return 0;
}
