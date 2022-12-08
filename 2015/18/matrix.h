#ifndef __MATRIX_H_
#define __MATRIX_H_

#include <vector>
#include <string>
using bool_matrix = std::vector<std::vector<bool>>;

bool_matrix read_matrix(std::string fn, int W, int H);
bool_matrix step(bool_matrix area, bool part2=true);


#endif // __MATRIX_H_
