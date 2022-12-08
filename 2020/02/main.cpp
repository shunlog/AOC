#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {

    {
        ifstream f("in.txt");
        string s;

        int valid = 0;
        while(getline(f, s)){
            stringstream ss(s);
            string nums, letter, pass;
            ss >> nums >> letter >> pass;
            int l1 = stoi(nums.substr(0, nums.find('-')));
            int l2 = stoi(nums.substr(nums.find('-')+1));
            letter.pop_back();

            int count = 0;
            for(char c : pass){
                if(c == letter[0]) count++;
            }
            if((l1 <= count) && (count <= l2)) valid++;
        }
        cout << "Silver: " << valid << '\n';
    }

    {
        ifstream f("in.txt");
        string s;

        int valid = 0;
        while(getline(f, s)){
            stringstream ss(s);
            string nums, letter, pass;
            ss >> nums >> letter >> pass;
            int l1 = stoi(nums.substr(0, nums.find('-')));
            int l2 = stoi(nums.substr(nums.find('-')+1));
            letter.pop_back();

            int count = 0;
            if(pass[l1-1] == letter[0]) count++;
            if(pass[l2-1] == letter[0]) count++;
            if(count == 1) valid++;
        }
        cout << "Gold: " << valid << '\n';
    }

    return 0;
}
