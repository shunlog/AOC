#include <iostream>

using namespace std;
using ll = long long;

ll p1 = 8252394;
ll p2 = 6269621;
// ll p1 = 5764801;
// ll p2 = 17807724;


int main(int argc, char *argv[]) {

    int s = 7; // subj num
    int ls = 0; // loop size

    ll v = 1;
    while(v != p1){
        v *= s;
        v %= 20201227;
        ls++;
    }
    cout << ls << '\n';

    v = 1;
    for(int i = 0; i < ls; i++){
        v *= p2;
        v %= 20201227;
    }
    cout << v << '\n';

    v = 1;
    ls = 0;
    while(v != p2){
        v *= s;
        v %= 20201227;
        ls++;
    }
    cout << ls << '\n';

    v = 1;
    for(int i = 0; i < ls; i++){
        v *= p1;
        v %= 20201227;
    }
    cout << v << '\n';

    return 0;
}
