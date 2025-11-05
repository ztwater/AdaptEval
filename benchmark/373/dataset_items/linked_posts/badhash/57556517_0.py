uint64_t xorshift(const uint64_t& n,int i){
  return n^(n>>i);
}
uint64_t hash(const uint64_t& n){
  uint64_t p = 0x5555555555555555ull; // pattern of alternating 0 and 1
  uint64_t c = 17316035218449499591ull;// random uneven integer constant; 
  return c*xorshift(p*xorshift(n,32),32);
}
