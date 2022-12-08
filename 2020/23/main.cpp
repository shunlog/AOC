#include <iostream>
#include <list>
#define log(x) cout << #x << " = " << x << '\n';
#define MIN 1
#define MAX 9
#define MOVES 100

using namespace std;

std::ostream& operator<<(std::ostream& ostr, const std::list<int>& list)
{
    for (auto &i : list) {
        ostr << " " << i;
    }
    return ostr;
}

list<int>::iterator find_it(list<int> &ls, int n){
    for(auto it = ls.begin(); it != ls.end(); it++){
        if(*it == n) return it;
    }
    return ls.end();
}

list<int>::iterator loop_advance(list<int>::iterator it, int n, list<int> &ls){
    while(n!=0){
        if(n > 0) n--; else n++;
        advance(it,1);
        if(it == ls.end())
          it = ls.begin();
    }
    return it;
}

void place3after(list<int>::iterator prev, list<int>::iterator dest, list<int> &ls){
    int d = *dest;
    dest = ls.erase(dest);

    list<int>::iterator from, to;
    from = loop_advance(prev, 1, ls);
    to = loop_advance(prev, 4, ls);

    ls.splice(dest, ls, from, to);
    ls.insert(from, d);
}

list<int>::iterator next_dest(list<int>::iterator prev, list<int> &ls){
    int n = *prev;
    while(n == *prev || n == *loop_advance(prev,1,ls)
          || n == *loop_advance(prev,2,ls) || n == *loop_advance(prev,3,ls)){
        if (n <= MIN) n = MAX;
        else n--;
    }
    return find_it(ls,n);
}

int main ()
{
    std::list<int> ls = {3, 8, 9, 1, 2, 5, 4, 6, 7};
    auto prev = ls.begin();
    std::cout << "ls: " << ls << "\n";

    list<int>::iterator dest;

    for(int i = 0; i < MOVES; i++){
        dest = next_dest(prev, ls);
        place3after(prev, dest, ls);
        log(*prev);
        log(*dest);
        prev = loop_advance(prev, 1, ls);
        std::cout << "ls: " << ls << "\n\n";
    }
}
