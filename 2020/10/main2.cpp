#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    vector<int> js(1,0);
    copy(istream_iterator<int>(cin), istream_iterator<int>(), back_inserter(js));
    sort(js.begin(), js.end());
    js.push_back(js.back() + 3);
    vector<int> diffs;
    adjacent_difference(js.begin(), js.end(), back_inserter(diffs));
    int64_t ones = count(diffs.begin() + 1, diffs.end(), 1);
    int64_t threes = count(diffs.begin() + 1, diffs.end(), 3);
    cout << "part 1: " << ones << " * " << threes << " = " << ones*threes << "\n";

    vector<int64_t> arrangements(js.size(), 0);
    arrangements.back() = 1;
    for(int i = js.size() - 1; i>=0; i--) {
        int jtage = js[i];
        int64_t as = arrangements[i];
        for(int j = i-1; j >= 0 && js[j] + 3 >= jtage; j--) {
            arrangements[j] += as;
        }
    }
    cout << "part 2: " << arrangements[0] << "\n";
}
