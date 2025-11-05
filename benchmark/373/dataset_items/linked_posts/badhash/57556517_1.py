   uint64_t const inline gfmul(const uint64_t& i,const uint64_t& j){           
     __m128i I{};I[0]^=i;                                                          
     __m128i J{};J[0]^=j;                                                          
     __m128i M{};M[0]^=0xb000000000000000ull;                                      
     __m128i X = _mm_clmulepi64_si128(I,J,0);                                      
     __m128i A = _mm_clmulepi64_si128(X,M,0);                                      
     __m128i B = _mm_clmulepi64_si128(A,M,0);                                      
     return A[0]^A[1]^B[1]^X[0]^X[1];                                              
   }
