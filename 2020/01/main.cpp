#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    
    ifstream f("in.txt");
    string s;
    vector<int> nums;
    while(getline(f, s)){
        nums.push_back(stoi(s));
    }

    bool found = false;
    for(int i=0; i<nums.size(); i++){
        for(int j=0; j<nums.size(); j++){
            if((i!=j) && nums[i]+nums[j]==2020){
                cout << "Silver: " << nums[i]*nums[j] << '\n';
                found = true;
                break;
            }
        }
        if(found)break;
    }

    found = false;
    for(int i=0; i<nums.size(); i++){
        for(int j=0; j<nums.size(); j++){
            for(int k=0; k<nums.size(); k++){
                if((i!=j!=k) && nums[i]+nums[j]+nums[k]==2020){
                    cout << "Gold: " << nums[i]*nums[j]*nums[k] << '\n';
                    found = true;
                    break;
                }
            } if(found)break;
        } if(found)break;
    }

    return 0;
}
