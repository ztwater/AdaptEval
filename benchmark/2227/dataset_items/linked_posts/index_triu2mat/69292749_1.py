#include<tuple>
#include<cmath>

// Linear indexing of the upper triangle, row by row
std::tuple<size_t, size_t> k2ij(size_t n, size_t k){
  size_t i = n - 2 - (size_t)std::floor(std::sqrt(4*n*(n-1) - (8*k) -7)/2.0 - 0.5);
  size_t j = k + i + 1 - n*(n-1)/2 + (n-i)*((n-i)-1)/2;
  return {i,j};
}

// Linear indexing of the upper triangle, diagonal by diagonal
std::tuple<size_t, size_t> d2ij(size_t n, size_t d){
  const auto [i, j] = k2ij(n, d);
  return {j-i-1, j}; // Conversion from row by row to diag by diag
}

#include<iostream>
#include<set>
int main(int argc, char** argv) {

  size_t n = 4;
  size_t top = n*(n-1)/2;

  for(size_t d=0; d<top; ++d){
    const auto [i,j] = d2ij(n, d);
    std::cout << "d2ij(" << n << ", " << d << ") = (" << i << ", " << j << ")" << std::endl;
  }

  return 0;
}
