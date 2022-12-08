#include <iostream>
#include <deque>
#include <vector>
#include <fstream>
#define FN "in.txt"
#define N 25

using namespace std;

int silver(const vector<int> &vec);
int gold(const vector<int> &vec, int invalid);

int main(int argc, char *argv[]) {

    ifstream f(FN);
    string line;
    vector<int> vec;
    while(getline(f,line))
        vec.push_back(stol(line));

    int silv = silver(vec);
    cout << "Silver: " << silv << '\n';
    cout << "Gold: " << gold(vec, silv) << '\n';

    return 0;
}

int silver(const vector<int> &vec){
    deque<int> deck;

    ifstream f(FN);
    string line;
    for(uint i = 0; i < N; i++){
        getline(f,line);
        int n = stoi(line);
        deck.push_back(n);
    }

    int invalid;
    while(getline(f,line)){
        int n = stoi(line);
        bool found = false;
        for(int i : deck){
            for(int j : deck){
                if(i != j && i + j == n){
                    found = true;
                }
            }
            if(found) break;
        }
        if(!found){
            invalid = n;
            break;
        }
        deck.push_back(n);
        deck.pop_front();
    }
    return invalid;
}

int gold(const vector<int> &vec, int invalid){
    long ans = 0;
    for(uint i = 0; i < vec.size(); i++){
        long sum = 0;
        long min = (unsigned long)~0 >> 1, max = 0;
        for(uint j = i; j < vec.size(); j++){
            sum += vec[j];
            if(vec[j] < min) min = vec[j];
            if(vec[j] > max) max = vec[j];

            if(sum > invalid)
                break;
            if(sum == invalid){
                ans = max + min;
                break;
            }
        }
        if(ans != 0){
            break;
        }
    }
    return ans;
}
